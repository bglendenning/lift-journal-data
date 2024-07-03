from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.orm import Session

from lift_journal_data.db.models import LiftSet
from lift_journal_data.schemas.lift_set import LiftSetCreateSchema


class LiftSetDAO:
    def __init__(self, session: Session, user_id: int):
        self.session = session
        self.user_id = user_id

    def create(self, lift_set: LiftSetCreateSchema):
        db_lift_set = LiftSet(
            user_id=lift_set.user_id,
            lift_id=lift_set.lift_id,
            repetitions=lift_set.repetitions,
            weight=lift_set.weight,
            date_performed=lift_set.date_performed,
            time_performed=lift_set.time_performed,
        )

        with self.session:
            self.session.add(db_lift_set)

            try:
                self.session.commit()
            except IntegrityError:
                self.session.rollback()
                db_lift_set = None
            else:
                self.session.refresh(db_lift_set)

        return db_lift_set

    def get_for_lift_set_id(self, lift_set_id: int):
        with self.session:
            try:
                db_lift_set = self.session.query(LiftSet).filter_by(user_id=self.user_id, id=lift_set_id).one()
            except NoResultFound:
                db_lift_set = None

        return db_lift_set

    def get_for_user_id(self):
        with self.session:
            try:
                db_lift_sets = (
                    self.session
                    .query(LiftSet)
                    .filter_by(user_id=self.user_id)
                    .order_by(LiftSet.date_performed.desc(), LiftSet.time_performed.desc())
                )
            except NoResultFound:
                db_lift_sets = None

        return db_lift_sets
