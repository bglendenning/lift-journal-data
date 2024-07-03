from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from lift_journal_data.db.models import Set
from lift_journal_data.schemas.set import SetCreateSchema


class SetDAO:
    def __init__(self, session: Session):
        self.session = session

    def create(self, lift_set: SetCreateSchema):
        db_set = Set(
            user_id=lift_set.user.id,
            lift_id=lift_set.lift.id,
            repetitions=lift_set.repetitions,
            weight=lift_set.weight,
            date_performed=lift_set.date_performed,
            time_performed=lift_set.time_performed,
        )

        with self.session:
            self.session.add(db_set)

            try:
                self.session.commit()
            except IntegrityError:
                self.session.rollback()
                db_set = None
            else:
                self.session.refresh(db_set)

        return db_set
