# pyrefly: ignore [missing-import]
import bcrypt
import jwt
from datetime import datetime, timedelta, timezone
from app.core.config import settings

# --- PASSWORD HASHING USING BCRYPT ---
# Hashing is a one-way cryptographic function. Once a password is hashed, it cannot be reversed.
# To verify, we hash the incoming password with the same parameters and compare the hashes.
# Bcrypt automatically generates a unique salt (random noise) for each password, protecting against rainbow table attacks.

def hash_password(password: str) -> str:
    """
    Hashes a plain text password using bcrypt.
    1. Converts string password into bytes.
    2. Generates a salt.
    3. Hashes password using the salt.
    4. Decodes the bytes back to a UTF-8 string for DB storage.
    """
    pw_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(pw_bytes, salt)
    return hashed_pw.decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies that a plain text password matches its stored bcrypt hash.
    1. Converts plain password to bytes.
    2. Converts stored hash back to bytes.
    3. Compares them using bcrypt.checkpw.
    """
    plain_bytes = plain_password.encode("utf-8")
    hashed_bytes = hashed_password.encode("utf-8")
    return bcrypt.checkpw(plain_bytes, hashed_bytes)


# --- JWT (JSON WEB TOKEN) AUTHENTICATION ---
# JWTs are stateless tokens used to authenticate clients.
# They consist of three parts separated by dots: Header, Payload, and Signature.
# The Signature is generated using a SECRET_KEY. Only our backend can verify it.
# This avoids querying the DB on every protected request.

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Generates a JWT access token containing a payload and signed with the secret key.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Standard JWT claim: 'exp' tells clients and libraries when the token expires
    to_encode.update({"exp": expire})
    
    # Encode token with payload, secret key, and algorithm
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> dict | None:
    """
    Decodes and verifies a JWT token.
    Returns the payload dictionary if valid, or None if expired/tampered.
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        # Token has expired
        return None
    except jwt.InvalidTokenError:
        # Token is invalid (e.g. signature doesn't match)
        return None
