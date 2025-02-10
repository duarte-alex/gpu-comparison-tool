import requests
from pydantic import BaseModel, ValidationError
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from cloud_providers import CloudProvider
from pathlib import Path
from aiohttp import ClientSession
import asyncio
from urllib.parse import quote

from cloud_providers.gcp.models import (
    ZONES,
    GCPAcceleratorTypeList,
    GCPAcceleratorAPIType,
    GCPZone,
    GPU,
)


class GoogleCloudProvider(CloudProvider):
    """Google Cloud Provider"""

    _credentials: Credentials

    def __init__(self, credential_paths: Path):
        self._credentials = Credentials.from_service_account_file(
            credential_paths,
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )

    def _oauth_token(self) -> str:
        """Returns the current oauth token for the credentials"""
        self._credentials.refresh(Request())

        return self._credentials.token

    # def _fetch_available_gpus(self) -> list[GCPAcceleratorType]:
    #     """Gets all the available GPUs in any zone

    #     ### Returns
    #     - list[GCPAcceleratorType]: A list of all the available GPUs in any zone
    #     """

    #     all_available_gpus: list[GCPAcceleratorType] = []

    #     for zone in ZONES[0:10]:
    #         url = f"https://compute.googleapis.com/compute/v1/projects/{self._credentials.project_id}/zones/{zone.name.value}/acceleratorTypes"
    #         headers = {"Authorization": f"Bearer {self._oauth_token()}"}
    #         response = requests.get(url, headers=headers)

    #         response_json = response.json()
    #         for item in response_json.get("items", []):
    #             item["zone"] = item.get("zone", "").split("/")[-1]
    #         accelerator_list = GCPAcceleratorTypeList.model_validate(response_json)

    #         for gpu in accelerator_list.items:
    #             if "NVIDIA" in gpu.description and "Workstation" not in gpu.description:
    #                 all_available_gpus.append(gpu)

    #     return all_available_gpus

    async def _fetch_available_gpus_async(self) -> list[GPU]:
        """Gets all the available GPUs in any zone asynchronously

        ### Returns
        - list[GCPAcceleratorType]: A list of all the available GPUs in any zone
        """

        async def _fetch_zone_gpus(session: ClientSession, zone: GCPZone) -> list[GPU]:
            """Fetches all the GPUs in a given zone."""

            url = f"https://compute.googleapis.com/compute/v1/projects/{self._credentials.project_id}/zones/{zone.name.value}/acceleratorTypes"
            headers = {"Authorization": f"Bearer {self._oauth_token()}"}
            async with session.get(url, headers=headers) as response:
                response_json = await response.json()

            accelerator_list = GCPAcceleratorTypeList.model_validate(response_json)

            gpus: list[GPU] = []
            for item in accelerator_list.items:
                if (
                    "NVIDIA" not in item.description
                    or "Workstation" in item.description
                ):
                    continue

                zone = item.zone.split("/")[-1]
                description = item.description.upper()

                gpus.append(
                    GPU(
                        name=description,
                        zone=zone,
                        maximumCardsPerInstance=item.maximumCardsPerInstance,
                    )
                )

            return gpus

        tasks: list[asyncio.Task[list[GPU]]] = []
        async with ClientSession() as session:
            for zone in ZONES:
                tasks.append(asyncio.create_task(_fetch_zone_gpus(session, zone)))

            results: list[list[GPU]] = await asyncio.gather(*tasks)

        all_available_gpus: list[GPU] = []
        for result in results:
            all_available_gpus.extend(result)

        return all_available_gpus

    def _preprocess_gpu(self, data):
        def preprocess_description(description):
            gpu_name, location = description, "Unknown"
            if "running in" in description:
                parts = description.split("running in")
            else:
                parts = description.split("in")

            gpu_name = parts[0].strip().lower()[:-4]

            if gpu_name == "nvidia tesla a100 80gb":
                gpu_name = "nvidia a100 80gb"
            elif gpu_name == "nvidia tesla a100":
                gpu_name = "nvidia a100 40gb"
            elif gpu_name == "nvidia tesla v100":
                gpu_name = "nvidia v100"
            elif gpu_name == "nvidia tesla t4":
                gpu_name = "nvidia t4"
            elif gpu_name == "h200 141gb":
                gpu_name = "nvidia h200 141gb"
            elif "plus" in gpu_name:
                gpu_name = gpu_name[:-5]

            return gpu_name

        return [
            {
                f"{preprocess_description(sku['description'])}|{region}": (
                    float(
                        sku.get("pricingInfo", [])[0]
                        .get("pricingExpression", {})
                        .get("tieredRates", [])[0]
                        .get("unitPrice", {})
                        .get("units", 0)
                    )
                    + sku.get("pricingInfo", [])[0]
                    .get("pricingExpression", {})
                    .get("tieredRates", [])[0]
                    .get("unitPrice", {})
                    .get("nanos", 0)
                    / 1e9
                )
            }
            for sku in data.get("skus", [])
            if sku.get("category", {}).get("resourceGroup", "") == "GPU"
            and sku["category"].get("usageType", []) == "OnDemand"
            and "Reserved" not in sku["description"]
            for region in sku.get("serviceRegions", [])
        ]

    def _fetch_gpu_pricing(self):
        url = "https://cloudbilling.googleapis.com/v1/services/6F81-5844-456A/skus"
        headers = {"Authorization": f"Bearer {self._oauth_token()}"}
        params = {}
        skus = []
        next_page_token = None

        while True:
            if next_page_token:
                params["pageToken"] = next_page_token

            response = requests.get(url, headers=headers, params=params)

            import json

            with open("response.json", "w") as f:
                json.dump(response.json(), f, indent=4)
            exit()

            if response.status_code == 200:
                data = response.json()
                skus.extend(self.preprocess_gpu(data))
                next_page_token = data.get("nextPageToken")
                if not next_page_token:
                    break
            else:
                print(f"Error: {response.status_code} \n {response.json()}")
                break

        return skus

    # ================================
    # Implement CloudProvider interface
    # ================================

    # def fetch_gpu_data(self) -> list[GPU]:
    #     pass
