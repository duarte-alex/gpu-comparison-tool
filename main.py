import os
import json
from cloud_providers.gcp import GoogleCloudProvider
from dotenv import load_dotenv
import asyncio


print("Loading environment variables...")
load_dotenv()
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
GCP_SERVICE_ACCOUNT_FILE = os.getenv("GCP_SERVICE_ACCOUNT_FILE")


# async def main():
    # GCP._fetch_gpu_pricing()


#asyncio.run(main())