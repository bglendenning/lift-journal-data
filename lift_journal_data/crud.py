from sqlalchemy.orm import Session

from lift_journal_data import models
from lift_journal_data.schemas import requests


def create_user(user: requests.UserCreate):
    with Session(models.engine) as session:
        db_user = models.User(email=user.email, password=user.password1)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)

    return db_user
