import argparse
import os

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from sqlalchemy import create_engine

db_engine = os.getenv("LIFT_JOURNAL_DB_ENGINE")
db_username = os.getenv("LIFT_JOURNAL_DB_USERNAME")
db_password = os.getenv("LIFT_JOURNAL_DB_PASSWORD")
db_server = os.getenv("LIFT_JOUNRAL_DB_SERVER")
db_name = os.getenv("LIFT_JOURNAL_DB_NAME")
db_url = f"{db_engine}://{db_username}:{db_password}@{db_server}/{db_name}"

engine = create_engine(db_url)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255))
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--create-tables',
        action=argparse.BooleanOptionalAction,
        help='Create tables in the database.',
    )
    args = parser.parse_args()

    if args.create_tables:
        create_tables()
