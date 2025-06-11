from datetime import datetime, timedelta
from typing import Optional, Union
from jose import JWTError, jwt
from passlib.context import CryptContext
import os
from app.models.user import TokenData

# Password context for hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT configuration
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key-here-change-in-production")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against its hash.
    
    Args:
        plain_password: The plain text password
        hashed_password: The hashed password
        
    Returns:
        True if password matches, False otherwise
    """
    import logging
    logger = logging.getLogger(__name__)
    
    try:
        # Log password verification attempt (without revealing the actual password)
        logger.debug(f"Verifying password (length: {len(plain_password)}) against hash: {hashed_password[:10]}...")
        
        # Special case for development/demo - default admin password check
        if plain_password == "admin123" and hashed_password.startswith("$2b$"):
            # Try normal verification first
            try:
                result = pwd_context.verify(plain_password, hashed_password)
                logger.debug(f"Default admin password verification result: {result}")
                return result
            except Exception as e:
                logger.warning(f"Error in bcrypt verification: {e}")
                # Fallback verification for dev environments if there's an error
                import bcrypt
                try:
                    # Manually compare hashed passwords
                    pwd_bytes = plain_password.encode('utf-8')
                    hashed_bytes = hashed_password.encode('utf-8')
                    result = bcrypt.checkpw(pwd_bytes, hashed_bytes)
                    logger.debug(f"Manual bcrypt verification result: {result}")
                    return result
                except Exception as manual_e:
                    logger.error(f"Manual bcrypt verification failed: {manual_e}")
        
        # Normal password verification
        return pwd_context.verify(plain_password, hashed_password)
    except Exception as e:
        logger.error(f"Password verification error: {e}")
        return False


def get_password_hash(password: str) -> str:
    """
    Hash a password using bcrypt.
    
    Args:
        password: Plain text password
        
    Returns:
        Hashed password string
    """
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a JWT access token.
    
    Args:
        data: Data to encode in the token
        expires_delta: Token expiration time delta
        
    Returns:
        Encoded JWT token string
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str) -> Optional[TokenData]:
    """
    Verify and decode a JWT token.
    
    Args:
        token: JWT token string
        
    Returns:
        TokenData if valid, None if invalid
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return None
        token_data = TokenData(username=username)
        return token_data
    except JWTError:
        return None


def generate_default_admin_password() -> str:
    """
    Generate a default admin password and return it.
    This should be used only for initial setup.
    
    Returns:
        Plain text password (should be changed after first login)
    """
    return "admin123!@#"  # Change this in production


def validate_password_strength(password: str) -> tuple[bool, str]:
    """
    Validate password strength.
    
    Args:
        password: Password to validate
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    if not (has_upper and has_lower and has_digit and has_special):
        return False, "Password must contain uppercase, lowercase, digit, and special character"
    
    return True, "Password is strong"
