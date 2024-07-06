from typing import Optional

from datetime import date, time

from pydantic import BaseModel


class LiftSetBaseSchema(BaseModel):
    lift_id: int
    repetitions: int
    weight: int
    date_performed: date
    time_performed: time

    class Config:
        from_attributes = True


class LiftSetCreateSchema(LiftSetBaseSchema):
    user_id: int


class LiftSetReadSchema(LiftSetBaseSchema):
    id: int


class LiftSetUpdateSchema(BaseModel):
    repetitions: Optional[int] = None
    weight: Optional[int] = None
    date_performed: Optional[date] = None
    time_performed: Optional[time] = None

    class Config:
        from_attributes = True
