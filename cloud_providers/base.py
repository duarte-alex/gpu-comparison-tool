from abc import ABC, abstractmethod
from models.gpu import GPU


class CloudProvider(ABC):
    """Abstract class for creating cloud provider gpu fetching class"""

    @abstractmethod
    async def get_gpu_data(self) -> list[GPU]:
        """Fetch and preprocess gpu data"""
        pass
