from pydantic import BaseModel


class TravelRequest(BaseModel):
    source: str
    destination: str
    budget: int
    date: str