import os
import json
# from cloud_providers import GoogleCloudProvider
from dotenv import load_dotenv

print("Loading environment variables...")
load_dotenv()
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
GCP_SERVICE_ACCOUNT_FILE = os.getenv("GCP_SERVICE_ACCOUNT_FILE")