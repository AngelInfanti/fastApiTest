from sqlalchemy import Column, Integer, String, Float
from app.database.database import Base



# Modelo SQLAlchemy para la base de datos
class CarDB(Base):
    __tablename__ = "cars"

    index = Column(Integer, primary_key=True, index=True)
    company = Column(String)
    style = Column(String)
    axles = Column(Float)
    length = Column(Float)
    engineType = Column(String)
    numberOfCylinders = Column(String)
    horsePower = Column(Integer)
    averageMileage = Column(Integer)
    price = Column(Float, nullable=True)
