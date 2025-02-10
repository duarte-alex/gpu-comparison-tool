from cloud_providers.gcp import GoogleCloudProvider
from config import Config
from time import time
import asyncio

config = Config()
GCP = GoogleCloudProvider(config.gcp_service_account_file)

# Asynchronous


async def main():
    # start = time()
    # gpus = await GCP._fetch_available_gpus_async()
    # end = time()

    # for gpu in gpus:
    #     print(gpu)

    # print("ASYNC:")
    # print(
    #     f"Time taken: {end - start} seconds. Average time per zone: {(end - start) / len(gpus)} seconds"
    # )

    GCP._fetch_gpu_pricing()


asyncio.run(main())
