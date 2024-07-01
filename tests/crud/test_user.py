from lift_journal_data.crud.user import UserDAO
from lift_journal_data.schemas.user import UserSchema
from tests.db import TestCaseDb


class TestUserDAO(TestCaseDb):
    email = "email@domain.tld"

    def test_create_user(self):
        with self.SessionLocal() as session:
            user = UserSchema(
                email=self.email,
                password="password",
            )
            db_user = UserDAO(session).create(user)
            self.assertEqual(db_user.email, self.email)

    def test_create_user_with_existing_email(self):
        with self.SessionLocal() as session:
            user = UserSchema(
                email=self.email,
                password="password",
            )
            UserDAO(session).create(user)

            # User exists for provided email
            db_user = UserDAO(session).create(user)
            self.assertIs(db_user, None)
