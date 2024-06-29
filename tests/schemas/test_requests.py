import unittest

from pydantic_core import ValidationError

from lift_journal_data.schemas import requests


class TestUserRegister(unittest.TestCase):
    def test_valid(self):
        # UserRegister is valid
        user_register = requests.UserRegister(
            email="test@domain.tld",
            password1="password",
            password2="password",
        )
        self.assertTrue(user_register.email == "test@domain.tld")
        self.assertTrue(user_register.password1 == "password")
        self.assertTrue(user_register.password2 == "password")

    def test_email_invalid(self):
        """UserRegister.email is invalid."""

        with self.assertRaises(ValidationError) as context:
            user_register = requests.UserRegister(
                email="email",
                password1="password",
                password2="password",
            )
        self.assertIn("email", str(context.exception))

        with self.assertRaises(ValidationError) as context:
            user_register = requests.UserRegister(
                email="",
                password1="password",
                password2="password",
            )
        self.assertIn("email", str(context.exception))

        with self.assertRaises(ValidationError) as context:
            user_register = requests.UserRegister(
                password1="password",
                password2="password",
            )
        self.assertIn("email", str(context.exception))

    def test_password_invalid(self):
        """UserRegister.password1 or password2 are invalid."""

        with self.assertRaises(ValidationError) as context:
            user_register = requests.UserRegister(
                email="email@domain.tld",
                password1="",
                password2="password",
            )
        self.assertIn("password1", str(context.exception))
