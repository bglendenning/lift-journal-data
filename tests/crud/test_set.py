from datetime import datetime

from lift_journal_data.crud.set import SetDAO
from lift_journal_data.crud.user import UserDAO
from lift_journal_data.db.manage import load_lifts
from lift_journal_data.db.models import Lift
from lift_journal_data.schemas.set import SetCreateSchema
from lift_journal_data.schemas.user import UserCreateSchema, UserReadSchema
from tests.db import TestCaseDb


class TestSetDAO(TestCaseDb):
    def setUp(self):
        super().setUp()

        user = UserCreateSchema(
            email="email@domain.tld",
            password="password",
        )
        self.db_user = UserDAO(self.SessionLocal()).create(user)

        load_lifts(self.SessionLocal(), Lift)

        with self.SessionLocal() as session:
            self.lift = session.query(Lift).filter_by(id=1).one()

    def test_create(self):
        user = UserReadSchema(
            id=self.db_user.id,
            email=self.db_user.email,
        )
        date_now = datetime.now().date()
        time_now = datetime.now().time()
        lift_set = SetCreateSchema(
            user_id=user.id,
            lift_id=self.lift.id,
            repetitions=1,
            weight=1,
            date_performed=date_now,
            time_performed=time_now,
        )
        db_set = SetDAO(self.SessionLocal()).create(lift_set)
        self.assertEqual(db_set.user_id, user.id)
        self.assertEqual(db_set.lift_id, self.lift.id)
        self.assertEqual(db_set.repetitions, 1)
        self.assertEqual(db_set.weight, 1)
        self.assertEqual(db_set.date_performed, date_now)
        self.assertEqual(db_set.time_performed, time_now)
