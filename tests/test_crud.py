import unittest

from lift_journal_data import crud, models
from lift_journal_data.schemas.user import UserCreate


class TestUserCrud(unittest.TestCase):
    email = "email@domain.tld"

    def setUp(self):
        models.create_tables()

    def tearDown(self):
        # Delete in-memory SQLite database
        models.engine.dispose()

    def test_create_user(self):
        with models.SessionLocal() as self.session:
            user = UserCreate(
                email=self.email,
                password1="password",
                password2="password",
            )
            db_user = crud.create_user(self.session, user)
            self.assertEqual(db_user.email, self.email)

    def test_create_user_with_existing_email(self):
        with models.SessionLocal() as self.session:
            user = UserCreate(
                email=self.email,
                password1="password",
                password2="password",
            )
            crud.create_user(self.session, user)

            # User exists for provided email
            db_user = crud.create_user(self.session, user)
            self.assertIs(db_user, None)
