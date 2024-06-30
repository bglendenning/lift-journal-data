import argparse
import json
import os
from pathlib import Path

from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

db_url = os.getenv("LIFT_JOURNAL_DB_URL")

if not db_url:
    db_engine = os.environ["LIFT_JOURNAL_DB_ENGINE"]
    db_username = os.environ["LIFT_JOURNAL_DB_USERNAME"]
    db_password = os.environ["LIFT_JOURNAL_DB_PASSWORD"]
    db_server = os.environ["LIFT_JOUNRAL_DB_SERVER"]
    db_name = os.environ["LIFT_JOURNAL_DB_NAME"]
    db_url = f"{db_engine}://{db_username}:{db_password}@{db_server}/{db_name}"

engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password: Mapped[str] = mapped_column(String(255))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, email={self.email!r})"


class Lift(Base):
    __tablename__ = "lift"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))

    def __repr__(self) -> str:
        return f"Lift(id={self.id!r}, name={self.name!r})"


def create_tables():
    Base.metadata.create_all(engine)


def drop_tables():
    Base.metadata.drop_all(engine)


def load_lifts():
    with SessionLocal() as session:
        with open(Path(os.path.dirname(__file__)) / "fixtures/lifts.json") as lifts_json:
            lifts = [Lift(name=lift["name"]) for lift in json.load(lifts_json)]

        session.add_all(lifts)
        session.commit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--create-tables",
        action=argparse.BooleanOptionalAction,
        help="Create tables in the database.",
    )
    parser.add_argument(
        "--drop-tables",
        action=argparse.BooleanOptionalAction,
        help="Drop all tables in the database.",
    )
    parser.add_argument(
        "--load-lifts",
        action=argparse.BooleanOptionalAction,
        help="Populate the lift table with various lifts",
    )
    args = parser.parse_args()

    if args.create_tables:
        create_tables()

    if args.drop_tables:
        drop_tables()

    if args.load_lifts:
        load_lifts()
