from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import hash_password


def create_user(db: Session, user: UserCreate) -> User:
    """
    Creates a new User record. Hashes the plain-text password before saving.
    """
    hashed_pw = hash_password(user.password)
    db_user = User(username=user.name, email=user.email, hashed_password=hashed_pw)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> User | None:
    """
    Fetches a user from the database by email address.
    """
    return db.query(User).filter(User.email == email).first()

def update_user(db: Session, user_id: int, user_update: UserUpdate) -> User | None:
    db_user = get_user(db, user_id)
    if db_user:
        if user_update.name is not None:
            db_user.username = user_update.name
        if user_update.email is not None:
            db_user.email = user_update.email
        if user_update.password is not None:
            db_user.hashed_password = hash_password(user_update.password)
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int) -> bool:
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False





