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

            if response.status_code == 200:
                gpus_available = response.json().get("items", [])
                for gpu in gpus_available:
                    if "NVIDIA" in gpu["description"]:
                        all_available_gpus.append({
                            "Zone": zone,
                            "Description": gpu["description"]})
            else:
                print(f"Error fetching GPUs for zone {zone}:")
                print(f"{response.status_code} \n {response.json()}")
                return []

        return all_available_gpus

    def fetch_gpu_pricing(self):
        """Query and preprocess GPUs pricing data"""
        pass

    def fetch_gpu(self):
        """Agregate available gpus with their pricing data"""
        pass

    def preprocess_gpu(self):
        """Helper method for preprocessing gpu data"""
        pass
