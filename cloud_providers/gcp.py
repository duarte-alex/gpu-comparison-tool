from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from .base import CloudProvider
import requests


class GoogleCloudProvider(CloudProvider):
    def __init__(self, project_id, service_account_file):
        super().__init__("Google Cloud")
        self.project_id = project_id
        self.service_account_file = service_account_file

    def oauth_token(self):
        credentials = Credentials.from_service_account_file(
                      self.service_account_file,
                      scopes=["https://www.googleapis.com/auth/cloud-platform"]
                      )
        credentials.refresh(Request())
        return credentials.token

    def fetch_gpu_available(self, zones):
        all_available_gpus = []

        for zone in zones:
            url = "https://compute.googleapis.com/compute/v1/projects/"
            url += f"{self.project_id}/zones/{zone}/acceleratorTypes"

            headers = {"Authorization": f"Bearer {self.oauth_token()}"}
            response = requests.get(url, headers=headers)

            if response.json().get("nextPageToken") != None:
                print("Page Token is needed for available GPUs")

            if response.status_code == 200:
                gpus_available = response.json().get("items", [])
                for gpu in gpus_available:
                    gpu_info = gpu["description"]
                    if "NVIDIA" in gpu_info and "Workstation" not in gpu_info:
                        all_available_gpus.append({
                            "Zone": zone,
                            "Description": gpu_info})
            else:
                print(f"Error fetching GPUs for zone {zone}:")
                print(f"{response.status_code} \n {response.json()}")
                return []

        return all_available_gpus

    def preprocess_gpu(self, data):
        def preprocess_description(description):
            gpu_name, location = description, "Unknown" 
            if "running in" in description:
                parts = description.split("running in")
            else:
                parts = description.split("in")

            gpu_name = parts[0].strip()
            location = parts[1].strip()
            if "for" in location:
                parts = location.split("for")
                location = parts[0].strip()      
        
            return gpu_name, location

        return [
            {
                "GPU": preprocess_description(sku["description"])[0],
                "Region(s)": ", ".join(sku.get("serviceRegions", [])),
                "Price (USD/hour)": sum([
                    float(pricing.get("unitPrice", {}).get("units", 0)) +
                    pricing.get("unitPrice", {}).get("nanos", 0) / 1e9
                    for pricing in sku.get("pricingInfo", [])[0].get("pricingExpression", {}).get("tieredRates", [])
                ])
            }
            for sku in data.get("skus", [])
            if sku.get("category", {}).get("resourceGroup", "") == "GPU" and sku["category"].get("usageType", []) == "OnDemand"
        ]


    def fetch_gpu_pricing(self):
        url = "https://cloudbilling.googleapis.com/v1/services/6F81-5844-456A/skus"
        headers = {"Authorization": f"Bearer {self.oauth_token()}"}
        skus = []
        next_page_token = None

        while True:
            params = {}
            if next_page_token:
                params["pageToken"] = next_page_token

            response = requests.get(url, headers=headers, params=params)
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
