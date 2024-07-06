import math

from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.orm import Session, Query

from lift_journal_data.db.models import LiftSet
from lift_journal_data.schemas.lift_set import LiftSetBaseSchema, LiftSetUpdateSchema


class LiftSetDAO:
    def __init__(self, session: Session, user_id: int):
        self.session = session
        self.user_id = user_id

    def create(self, lift_set: LiftSetBaseSchema):
        db_lift_set = LiftSet(user_id=self.user_id, **lift_set.model_dump())

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

    def get_for_user_id(self, page: int = 1, page_size: int = 100):
        if page < 1:
            raise ValueError("page must be greater than 0")

        limit, offset = self.get_limit_offset(page, page_size)

        with self.session:
            db_lift_sets = self.session.query(LiftSet).filter_by(user_id=self.user_id)
            count, pages = self.get_pages(db_lift_sets, page_size)
            db_lift_sets = (
                db_lift_sets
                .order_by(LiftSet.date_performed.desc(), LiftSet.time_performed.desc())
                .limit(limit)
                .offset(offset)
            )

        return db_lift_sets, count, pages

    def update_for_lift_set_id(self, lift_set_id: int, lift_set: LiftSetUpdateSchema):
        with self.session:
            rows_updated = (
                self.session.query(LiftSet)
                .filter_by(id=lift_set_id, user_id=self.user_id)
                .update({key: value for key, value in lift_set.model_dump().items() if value})
            )
            self.session.commit()

            return rows_updated

    def delete_for_lift_set_id(self, lift_set_id):
        with self.session:
            try:
                db_lift_set = self.session.query(LiftSet).filter_by(user_id=self.user_id, id=lift_set_id).one()
            except NoResultFound:
                return None

        self.session.delete(db_lift_set)
        self.session.commit()

        return True

    @classmethod
    def get_limit_offset(cls, page: int, page_size: int):
        limit: int = page_size
        offset: int = (page - 1) * page_size

        return limit, offset

    @classmethod
    def get_pages(cls, db_lift_sets: Query, page_size: int):
        count = db_lift_sets.count()
        pages = math.ceil(count / page_size)

        return count, pages
