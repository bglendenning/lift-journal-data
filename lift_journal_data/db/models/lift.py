from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from lift_journal_data.db import Base


class Lift(Base):
    __tablename__ = "lift"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), nullable=False)

    def __repr__(self) -> str:
        return f"Lift(id={self.id!r}, name={self.name!r})"
