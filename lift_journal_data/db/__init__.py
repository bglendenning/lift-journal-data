import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class LiftJournalData:
    def __init__(self):
        self.DB_URL = os.getenv("LIFT_JOURNAL_DATA_DB_URL")

        if not self.DB_URL:
            self.DB_ENGINE = os.environ["LIFT_JOURNAL_DATA_DB_ENGINE"]
            self.DB_USERNAME = os.environ["LIFT_JOURNAL_DATA_DB_USERNAME"]
            self.DB_PASSWORD = os.environ["LIFT_JOURNAL_DATA_DB_PASSWORD"]
            self.DB_SERVER = os.environ["LIFT_JOURNAL_DATA_DB_SERVER"]
            self.DB_NAME = os.environ["LIFT_JOURNAL_DATA_DB_NAME"]
            self.DB_URL = f"{self.DB_ENGINE}://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_SERVER}/{self.DB_NAME}"

        self.engine = create_engine(self.DB_URL)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)


class Base(DeclarativeBase):
    pass
