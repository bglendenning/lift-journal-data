from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from lift_journal_data import models
from lift_journal_data.schemas.user import UserCreate


def create_user(session: Session, user: UserCreate):
    db_user = models.User(email=user.email, password=user.password1)
    session.add(db_user)

    try:
        session.commit()
    except IntegrityError:
        # Attempted to create User with non-unique email
        session.rollback()
        db_user = None
    else:
        session.refresh(db_user)

    return db_user
