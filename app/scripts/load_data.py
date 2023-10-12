import pandas as pd
from sqlalchemy.orm import Session
from app.models.cars import CarDB
from app.database.database import SessionLocal

# Obtén la ruta absoluta del archivo CSV
csv_path = 'data/Automobile_data.csv'


def load_data():
    db = SessionLocal()
    data = pd.read_csv(csv_path)

    for _, row in data.iterrows():
        # Verifica si ya existe un registro con la misma compañía y precio
        existing_car = db.query(CarDB).filter(
            CarDB.compania == row['compania'],
            CarDB.precio == row['precio']
        ).first()

        if existing_car is None:
            db_car = CarDB(**row)
            db.add(db_car)

    db.commit()

if __name__ == "__main__":
    load_data()
