from lift_journal_data.crud.user import UserDAO
from lift_journal_data.schemas.user import UserSchema
from tests.db import TestCaseDb


class TestUserDAO(TestCaseDb):
    user = UserSchema(
        email="email@domain.tld",
        password="password",
    )

    def test_create(self):
        with self.SessionLocal() as session:
            db_user = UserDAO(session).create(self.user)

        self.assertEqual(db_user.email, self.user.email)

    def test_create_with_existing_email(self):
        with self.SessionLocal() as session:
            UserDAO(session).create(self.user)
            db_user = UserDAO(session).create(self.user)

        self.assertIs(db_user, None)

    def test_get_for_email_password(self):
        with self.SessionLocal() as session:
            UserDAO(session).create(self.user)
            db_user = UserDAO(session).get_for_email_password(self.user)

        self.assertEqual(db_user.email, self.user.email)
        self.assertEqual(db_user.password, self.user.password)

        with self.SessionLocal() as session:
            db_user = UserDAO(session).get_for_email_password(
                UserSchema(
                    email=self.user.email, password="incorrect password"
                ),
            )

        self.assertEqual(db_user, None)
