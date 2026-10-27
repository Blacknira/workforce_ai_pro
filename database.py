from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# --- DATABASE URL ---
# MySQL Format: mysql+pymysql://username:password@localhost/dbname
# Unga MySQL password ah maathikanum

DB_USER = "root"
DB_PASSWORD = "Manira2909*"  # <--- UNGA MYSQL PASSWORD INGHA MAATHU MA
DB_HOST = "localhost"
DB_NAME = "workforce_ai"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Engine create pannrom
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # Connection check pannum
    echo=False  # SQL query console la kaatadhu
)

# Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base - Ella model ithula irundhu varum
Base = declarative_base()

# Dependency - FastAPI ku DB session kudukka
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()