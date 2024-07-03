from datetime import date, time

from pydantic import BaseModel

from lift_journal_data.schemas.lift import LiftSchema
from lift_journal_data.schemas.user import UserReadSchema


class SetBaseSchema(BaseModel):
    lift_id: int
    repetitions: int
    weight: int
    date_performed: date
    time_performed: time

    class Config:
        from_attributes = True


class SetCreateSchema(SetBaseSchema):
    user_id: int
