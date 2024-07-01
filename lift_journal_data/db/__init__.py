import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DB_URL = os.getenv("LIFT_JOURNAL_DATA_DB_URL")

if not DB_URL:
    DB_ENGINE = os.environ["LIFT_JOURNAL_DATA_DB_ENGINE"]
    DB_USERNAME = os.environ["LIFT_JOURNAL_DATA_DB_USERNAME"]
    DB_PASSWORD = os.environ["LIFT_JOURNAL_DATA_DB_PASSWORD"]
    DB_SERVER = os.environ["LIFT_JOUNRAL_DATA_DB_SERVER"]
    DB_NAME = os.environ["LIFT_JOURNAL_DATA_DB_NAME"]
    DB_URL = f"{DB_ENGINE}://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass
