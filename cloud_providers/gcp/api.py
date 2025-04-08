from aiohttp import ClientSession
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from .models import GCPAcceleratorTypeList, GCPZone, GPU, GCPZoneNames, GCPGPUNames
from .zones import ZONES
import asyncio

def get_oauth_token(credentials: Credentials) -> str:
    credentials.refresh(Request())
    return credentials.token

async def fetch_gpus_in_zone(session: ClientSession, token: str, project_id: str, zone: GCPZone) -> list[GPU]:
    url = f"https://compute.googleapis.com/compute/v1/projects/{project_id}/zones/{zone.name.value}/acceleratorTypes"
    headers = {"Authorization": f"Bearer {token}"}

    async with session.get(url, headers=headers) as response:
        response_json = await response.json()

    gpus: list[GPU] = []
    data = GCPAcceleratorTypeList.model_validate(response_json)
    for item in data.items or []:
        if "NVIDIA" in item.description and "Workstation" not in item.description:
            gpus.append(GPU(
                name=item.description.upper(),
                zone=item.zone.split("/")[-1],
                maximumCardsPerInstance=item.maximumCardsPerInstance
            ))
    return gpus

async def fetch_all_available_gpus(credentials: Credentials, project_id: str) -> list[GPU]:
    token = get_oauth_token(credentials)
    tasks = []

    async with ClientSession() as session:
        for zone in ZONES:
            task = fetch_gpus_in_zone(session, token, project_id, zone)
            tasks.append(task)
        results = await asyncio.gather(*tasks)

    return [gpu for sublist in results for gpu in sublist]
