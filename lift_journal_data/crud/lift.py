from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from lift_journal_data.db.models import Lift


class LiftDAO:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        with self.session:
            return self.session.query(Lift).order_by(Lift.name.asc()).all()

    def get_for_id(self, lift_id: int):
        with self.session:
            try:
                db_lift = self.session.query(Lift).filter_by(id=lift_id).one()
            except NoResultFound:
                db_lift = None

        return db_lift
