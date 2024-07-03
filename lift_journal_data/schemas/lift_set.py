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
