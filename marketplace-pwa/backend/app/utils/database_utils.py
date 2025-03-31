from app.utils.auth import get_password_hash
from app.models.user import User
from sqlalchemy.orm import Session

def create_admin_user(db: Session, username: str, password: str):
    """
    Creates a new admin user in the database.

    Args:
        db (Session): SQLAlchemy database session.
        username (str): The username of the admin.
        password (str): The plain-text password of the admin.

    Returns:
        User: The newly created admin user.
    """
    hashed_password = get_password_hash(password)
    new_user = User(username=username, password_hash=hashed_password, is_admin=True)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user