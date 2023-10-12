from typing import List, Optional
from pydantic import BaseModel

# Modelo Pydantic para las solicitudes de FastAPI
class CarBase(BaseModel):
    company: str
    style: str
    axles: int
    length: int
    engineType: str
    numberOfCylinders: str
    horsePower: int
    averageMileage: float
    price: Optional[float]

class CarsCreate(BaseModel):
     cars: List[CarBase]

# Modelo Pydantic para las respuestas de FastAPI
class Car(CarBase):
    index: int

    class Config:
        orm_mode = True