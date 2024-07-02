from datetime import date, time

from sqlalchemy import Date, ForeignKey, SmallInteger, String, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

from lift_journal_data.db import Base


class Set(Base):
    __tablename__ = "set"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    user: Mapped["lift_journal_data.db.models.user.User"] = relationship(back_populates="sets")
    lift_id: Mapped[int] = mapped_column(ForeignKey("lift.id"), nullable=False)
    lift: Mapped["lift_journal_data.db.models.lift.Lift"] = relationship()
    repetitions: Mapped[int] = mapped_column(SmallInteger(), nullable=False)
    weight: Mapped[int] = mapped_column(SmallInteger(), nullable=False)
    date_performed: Mapped[date] = mapped_column(Date(), nullable=False)
    time_performed: Mapped[time] = mapped_column(Time(), nullable=False)
