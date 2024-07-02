from datetime import date, time

from pydantic import BaseModel

from lift_journal_data.schemas.lift import LiftSchema


class SetSchema(BaseModel):
    lift: LiftSchema
    repetitions: int
    weight: int
    date_performed: date
    time_performed: time
