from fastapi import HTTPException, Security
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext

# Initialize FastAPI's HTTPBasic security
security = HTTPBasic()

# Initialize Passlib's CryptContext for hashing passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to hash a password
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# Function to verify a password against its hash
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Function to authenticate admin users
def authenticate_admin(credentials: HTTPBasicCredentials, db_session):
    # Query the database for the admin user
    user = db_session.query(User).filter(User.username == credentials.username, User.is_admin == True).first()
    if not user or not verify_password(credentials.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return True