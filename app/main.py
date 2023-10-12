from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.routers.cars import get_cars ,create_car
from app.schemas.cars import Car, CarBase, CarsCreate
from app.models.cars import CarDB, Base
from app.database.database import SessionLocal, engine

""" from app.scripts.load_data import load_data """
import pandas as pd

Base.metadata.create_all(bind=engine)

""" load_data() """
csv_path = 'data/Automobile_data.csv'

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def index():
    return {"message": "VenEmergencia API Test"}

@app.post("/loadCars/", status_code=201)
def load_cars(db: Session = Depends(get_db)):
    data = pd.read_csv(csv_path)
    dataClean = []
    unique_cars = set()
    print(len(data))
    for _, row in data.iterrows():

        car_data = CarBase(
            company=row['compania'],
            style=row['estilo'],
            axles=row['ejes'],
            length=row['largo'],
            engineType=row['tipo-motor'],
            numberOfCylinders=row['numero-de-cilindros'],
            horsePower=row['caballos-de-fuerza'],
            averageMileage=row['kilimetraje-promedio'],
            price=row['precio']
        )
        car_key = (car_data.company, car_data.style)
        if car_key not in unique_cars:
            db_car = CarDB(**car_data.dict())
            dataClean.append(db_car)
            unique_cars.add(car_key)

    print(len(dataClean))
    return create_car(db=db, db_cars=dataClean)

@app.get("/cars/", response_model=list[Car])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = get_cars(db, skip=skip, limit=limit)
    return items


