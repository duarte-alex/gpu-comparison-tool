from pathlib import Path
from google.oauth2.service_account import Credentials
from cloud_providers.base import CloudProvider
from cloud_providers.gcp.api import fetch_all_available_gpus
from cloud_providers.gcp.models import GPU

class GoogleCloudProvider(CloudProvider):
    def __init__(self, credentials_path: Path):
        self._credentials = Credentials.from_service_account_file(
            credentials_path,
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )

    async def get_available_gpus(self) -> list[GPU]:
        return await fetch_all_available_gpus(
            self._credentials, self._credentials.project_id)