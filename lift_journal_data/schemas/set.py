from datetime import date, time

from pydantic import BaseModel

from lift_journal_data.schemas.lift import LiftSchema
from lift_journal_data.schemas.user import UserReadSchema


class SetBaseSchema(BaseModel):
    repetitions: int
    weight: int
    date_performed: date
    time_performed: time


class SetCreateSchema(SetBaseSchema):
    user: UserReadSchema
    lift: LiftSchema
