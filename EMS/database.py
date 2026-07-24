from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = ("postgresql+psycopg2://postgres:dushy123@localhost:5432/expense")
engine = create_engine(DATABASE_URL,echo=True)
SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)
# All models inherit from this
Base = declarative_base()