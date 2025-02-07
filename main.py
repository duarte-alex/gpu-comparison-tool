import os
from cloud_providers import GoogleCloudProvider
from dotenv import load_dotenv
import json


def save_to_json(filename, data):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
        print(f"Saved data to {filename}")


load_dotenv()
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
GCP_SERVICE_ACCOUNT_FILE = os.getenv("GCP_SERVICE_ACCOUNT_FILE")

ZONES = [
    # US Central
    "us-central1-a", "us-central1-b", "us-central1-c", "us-central1-f",

    # US East
    "us-east1-b", "us-east1-c", "us-east1-d",
    "us-east4-a", "us-east4-b", "us-east4-c",

    # US West
    "us-west1-a", "us-west1-b",
    "us-west2-b", "us-west2-c",
    "us-west4-a", "us-west4-b",

    # Europe
    "europe-west1-b", "europe-west1-c", "europe-west1-d",
    "europe-west2-a", "europe-west2-b",
    "europe-west3-b",
    "europe-west4-a", "europe-west4-b", "europe-west4-c",
    "europe-west6-b",

    # Asia-Pacific
    "asia-east1-a", "asia-east1-b", "asia-east1-c",
    "asia-northeast1-a", "asia-northeast1-b", "asia-northeast1-c",
    "asia-northeast3-a", "asia-northeast3-b", "asia-northeast3-c",
    "asia-south1-a", "asia-south1-b", "asia-south1-c",
    "asia-southeast1-a", "asia-southeast1-b", "asia-southeast1-c",
    "asia-southeast2-a", "asia-southeast2-b",

    # Australia
    "australia-southeast1-a", "australia-southeast1-b", "australia-southeast1-c",

    # South America
    "southamerica-east1-c"
]


GCP = GoogleCloudProvider(GCP_PROJECT_ID, GCP_SERVICE_ACCOUNT_FILE)
gcp_gpu_available = GCP.fetch_gpu_available(ZONES)

save_to_json("gcp_gpu_available.json", gcp_gpu_available)
