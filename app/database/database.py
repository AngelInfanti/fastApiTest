from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configura la URL de la base de datos. Asegúrate de reemplazar 'db_url' con la URL real de tu base de datos.
db_url = "sqlite:///./venemergencia-test.db"

# Crea una instancia del motor SQLAlchemy
engine = create_engine(
    db_url, connect_args={"check_same_thread": False}
)

# Crea una función para obtener una sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define la clase Base para declarar modelos SQLAlchemy
Base = declarative_base()