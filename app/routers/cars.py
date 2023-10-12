
from sqlalchemy.orm import Session
from app.schemas.cars import CarsCreate
from app.models.cars import CarDB


def get_cars(db: Session, skip: int = 0, limit: int = 100):
    return db.query(CarDB).offset(skip).limit(limit).all()

def create_car(db: Session, db_cars: CarsCreate):
    db.add_all(db_cars)
    db.commit()
    return {"message": f"{len(db_cars)} cars loaded successfully"}

def get_fistFive_and_lastFive(db: Session):
    return db.query(CarDB).order_by(CarDB.index).limit(5).all(), db.query(CarDB).order_by(CarDB.index.desc()).limit(5).all()
