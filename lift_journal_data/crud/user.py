from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.orm import Session

from lift_journal_data.db.models import User
from lift_journal_data.schemas.user import UserSchema


class UserDAO:
    def __init__(self, session: Session):
        self.session = session

    def create(self, user: UserSchema):
        db_user = User(email=user.email, password=user.password)
        self.session.add(db_user)

        try:
            self.session.commit()
        except IntegrityError:
            # Attempted to create User with non-unique email
            self.session.rollback()
            db_user = None
        else:
            self.session.refresh(db_user)

        return db_user

    def get_for_email(self, email: str):
        try:
            db_user = self.session.query(User).filter_by(email=email).one()
        except NoResultFound:
            db_user = None

        return db_user
