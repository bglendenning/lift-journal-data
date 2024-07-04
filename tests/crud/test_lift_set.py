from datetime import datetime, timedelta

from lift_journal_data.crud.lift_set import LiftSetDAO
from lift_journal_data.crud.user import UserDAO
from lift_journal_data.db.manage import load_lifts
from lift_journal_data.db.models import Lift
from lift_journal_data.schemas.lift_set import LiftSetBaseSchema
from lift_journal_data.schemas.user import UserCreateSchema, UserReadSchema
from tests.db import TestCaseDb


class TestLiftSetDAO(TestCaseDb):
    def setUp(self):
        super().setUp()

        user = UserCreateSchema(
            email="email@domain.tld",
            password="password",
        )
        self.db_user = UserDAO(self.SessionLocal()).create(user)

        load_lifts(self.SessionLocal())

        with self.SessionLocal() as session:
            self.lift = session.query(Lift).filter_by(id=1).one()

    def test_create(self):
        user = UserReadSchema(
            id=self.db_user.id,
            email=self.db_user.email,
        )
        date_now = datetime.now().date()
        time_now = datetime.now().time()
        lift_set = LiftSetBaseSchema(
            lift_id=self.lift.id,
            repetitions=1,
            weight=1,
            date_performed=date_now,
            time_performed=time_now,
        )

        with self.SessionLocal() as session:
            db_lift_set = LiftSetDAO(session, self.db_user.id).create(lift_set)

        self.assertEqual(db_lift_set.user_id, user.id)
        self.assertEqual(db_lift_set.lift_id, self.lift.id)
        self.assertEqual(db_lift_set.repetitions, 1)
        self.assertEqual(db_lift_set.weight, 1)
        self.assertEqual(db_lift_set.date_performed, date_now)
        self.assertEqual(db_lift_set.time_performed, time_now)

    def test_get_for_lift_set_id(self):
        with self.SessionLocal() as session:
            LiftSetDAO(session, self.db_user.id).create(
                LiftSetBaseSchema(
                    lift_id=self.lift.id,
                    repetitions=1,
                    weight=1,
                    date_performed=datetime.now().date(),
                    time_performed=datetime.now().time(),
                )
            )
            db_lift_set = LiftSetDAO(session, self.db_user.id).get_for_lift_set_id(1)

        self.assertEqual(db_lift_set.user_id, self.db_user.id)

    def test_get_for_user_id(self):
        user2 = UserDAO(self.SessionLocal()).create(UserCreateSchema(email="email2@domain.tld", password="password"))
        with self.SessionLocal() as session:
            LiftSetDAO(session, user2.id).create(
                LiftSetBaseSchema(
                    lift_id=self.lift.id,
                    repetitions=1,
                    weight=1,
                    date_performed=datetime.now().date(),
                    time_performed=datetime.now().time(),
                )
            )

            for i in range(2):
                LiftSetDAO(session, self.db_user.id).create(
                    LiftSetBaseSchema(
                        lift_id=self.lift.id,
                        repetitions=1,
                        weight=1,
                        date_performed=datetime.now().date(),
                        time_performed=(datetime.now() + timedelta(seconds=i)).time(),
                    )
                )

            db_lift_sets = LiftSetDAO(session, self.db_user.id).get_for_user_id()

        self.assertEqual(db_lift_sets.count(), 2)

        with self.SessionLocal() as session:
            LiftSetDAO(session, self.db_user.id).create(
                LiftSetBaseSchema(
                    lift_id=self.lift.id,
                    repetitions=1,
                    weight=1,
                    date_performed=(datetime.now() + timedelta(days=1)).date(),
                    time_performed=datetime.now().time(),
                )
            )

        # Ordered by date descending, time descending
        self.assertEqual(db_lift_sets.count(), 3)
        self.assertGreater(db_lift_sets[0].date_performed, db_lift_sets[1].date_performed)
        self.assertGreater(db_lift_sets[1].time_performed, db_lift_sets[2].time_performed)

    def test_delete_for_lift_set_id(self):
        with self.SessionLocal() as session:
            lift_set_dao = LiftSetDAO(session, self.db_user.id)
            db_lift_set = lift_set_dao.create(
                LiftSetBaseSchema(
                    lift_id=self.lift.id,
                    repetitions=1,
                    weight=1,
                    date_performed=datetime.now().date(),
                    time_performed=datetime.now().time(),
                )
            )
            self.assertEqual(lift_set_dao.get_for_user_id().count(), 1)
            lift_set_dao.delete_for_lift_set_id(db_lift_set.id)
            self.assertEqual(lift_set_dao.get_for_user_id().count(), 0)
