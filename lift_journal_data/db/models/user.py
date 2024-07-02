from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from lift_journal_data.db import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    sets: Mapped[list["lift_journal_data.db.models.set.Set"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, email={self.email!r})"
