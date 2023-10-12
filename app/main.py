from typing import List, Tuple
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.routers.cars import get_cars, get_fistFive_and_lastFive, create_car
from app.schemas.cars import Car, CarBase
from app.models.cars import CarDB, Base
from app.database.database import SessionLocal, engine

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

@app.get("/getAllCars/", response_model=list[Car])
def read_cards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cars = get_cars(db, skip=skip, limit=limit)
    return cars

# a. Imprima las primeras cinco (5) y las últimas cinco (5) líneas
@app.get("/getFirstFiveAndLastFive", response_model=dict)
def read_cards(db: Session = Depends(get_db)):
    firstFive, lastFive = get_fistFive_and_lastFive(db)
    return {"firstFive": firstFive, "lastFive": lastFive}

# b. Encuentra la compañía de autos más costosa
@app.get("/mostExpensiveCompany")
def find_most_expensive_company(db: Session = Depends(get_db)):
    most_expensive_company = db.query(
        CarDB.company,
        func.sum(CarDB.price).label("total_price")) \
        .group_by(CarDB.company) \
        .order_by(func.sum(CarDB.price).desc()) \
        .first()

    if most_expensive_company:
        company, total_price = most_expensive_company
        return {"most_expensive_company": company, "total_price": total_price}
    else:
        return {"most_expensive_company": None, "total_price": None}


# c. Imprime todos los detalles de los autos Toyota
@app.get("/detailsToyotaCars")
def find_toyota_cars(db: Session = Depends(get_db)):
    toyota_cars = db.query(CarDB.style).filter(
        func.upper(CarDB.company) == "TOYOTA",
    ).all()
    return [result[0] for result in toyota_cars]

# d. Cuente el número total de autos por compañía
@app.get("/countCarsByCompany")
def count_cars_by_company(company: str = '', db: Session = Depends(get_db)):
    if company != '':
        cars_by_company = db.query(
            CarDB.company,
            func.count(CarDB.company).label("total_cars")) \
            .filter(func.upper(CarDB.company) == func.upper(company)) \
            .group_by(CarDB.company) \
            .all()
    else:
        cars_by_company = db.query(
            CarDB.company,
            func.count(CarDB.company).label("total_cars")) \
            .group_by(CarDB.company) \
            .all()
    return [
        {
            "company": company,
            "total_cars": total_cars
        }
    for company, total_cars in cars_by_company]

# e. Encuentre el precio más alto por cada compañía
@app.get("/maxPriceByCompany")
def find_max_price_by_company(company: str = '', db: Session = Depends(get_db)):
    if company != '':
        max_price_by_company = db.query(
            CarDB.company,
            func.max(CarDB.price).label("max_price")) \
            .filter(func.upper(CarDB.company) == func.upper(company)) \
            .group_by(CarDB.company) \
            .all()
    else:
        max_price_by_company = db.query(
            CarDB.company,
            func.max(CarDB.price).label("max_price")) \
            .group_by(CarDB.company) \
            .all()
    return [
        {
            "company": company,
            "max_price": max_price
        }
    for company, max_price in max_price_by_company]

# f. Encuentre el kilometraje promedio de cada compañía
@app.get("/averageMileageByCompany")
def find_average_mileage_by_company(company: str = '', db: Session = Depends(get_db)):
    if company != '':
        average_mileage_by_company = db.query(
            CarDB.company,
            func.avg(CarDB.averageMileage).label("average_mileage")) \
            .filter(func.upper(CarDB.company) == func.upper(company)) \
            .group_by(CarDB.company) \
            .all()
    else:
        average_mileage_by_company = db.query(
            CarDB.company,
            func.avg(CarDB.averageMileage).label("average_mileage")) \
            .group_by(CarDB.company) \
            .all()
    return [
        {
            "company": company,
            "average_mileage": average_mileage
        }
    for company, average_mileage in average_mileage_by_company]

# g. Ordenar todos los carros por la columna Precio
@app.get("/orderByPrice")
def order_by_price(db: Session = Depends(get_db)):
    cars = db.query(CarDB).order_by(CarDB.price).all()
    return cars


@app.post("/loadCars/", status_code=201)
def load_cars(db: Session = Depends(get_db)):
    data = pd.read_csv(csv_path)
    dataClean = []
    unique_cars = set()
    for _, row in data.iterrows():

        existing_car = db.query(CarDB).filter(
                CarDB.company == row['compania'],
                CarDB.style == row['estilo']
        ).first()

        if existing_car is None:
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

    return create_car(db=db, db_cars=dataClean)

