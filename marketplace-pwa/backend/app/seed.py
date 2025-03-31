from sqlalchemy.orm import Session
from app.utils.database_utils import create_admin_user
from app.database import SessionLocal

# Seed the database with an initial admin user
def seed_database(username: str, password: str):
    db: Session = SessionLocal()
    try:
        create_admin_user(db, username=username, password=password)
        print("Admin user created successfully!")
    except Exception as e:
        print(f"Error seeding database: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    # Example usage: Replace with actual input or environment variables as needed
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    seed_database(username, password)    