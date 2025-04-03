from abc import ABC, abstractmethod
from typing import List
from cloud_providers.gcp.models import GPU

class CloudProvider(ABC):
    @abstractmethod
    async def get_available_gpus(self) -> List[GPU]:
        pass