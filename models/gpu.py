from pydantic import BaseModel


class GPU(BaseModel):
    name: str
    zone: str
    maximumCardsPerInstance: int
    price: float

    def __str__(self):
        return f"{self.name} ({self.zone}) - {self.price}"
