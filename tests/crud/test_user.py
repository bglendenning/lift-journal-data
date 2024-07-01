from lift_journal_data.crud.user import create_user
from lift_journal_data.schemas.user import UserSchema
from tests.db import TestCaseDb


class TestCrudUser(TestCaseDb):
    email = "email@domain.tld"

    def test_create_user(self):
        with self.SessionLocal() as session:
            user = UserSchema(
                email=self.email,
                password1="password",
                password2="password",
            )
            db_user = create_user(session, user)
            self.assertEqual(db_user.email, self.email)

    def test_create_user_with_existing_email(self):
        with self.SessionLocal() as session:
            user = UserSchema(
                email=self.email,
                password1="password",
                password2="password",
            )
            create_user(session, user)

            # User exists for provided email
            db_user = create_user(session, user)
            self.assertIs(db_user, None)
