from datetime import date, time

from pydantic import BaseModel

from lift_journal_data.schemas.lift import LiftSchema
from lift_journal_data.schemas.user import UserReadSchema


class SetCreateSchema(BaseModel):
    user: UserReadSchema
    lift: LiftSchema
    repetitions: int
    weight: int
    date_performed: date
    time_performed: time
