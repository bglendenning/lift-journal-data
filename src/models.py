import argparse

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from sqlalchemy import create_engine

engine = create_engine("postgresql://lift_journal:lift_journal@localhost/lift_journal")


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
