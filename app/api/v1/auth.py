from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.crud.user import get_user_by_email
from app.core.security import verify_password, create_access_token
from app.schemas.user import Token

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

# Swagger Authorize button sends form-data with fields 'username' and 'password'
@router.post("/login", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    Authenticate a user using their email (sent as 'username') and password.
    Returns a JWT access token.
    """
    # 1. Fetch user by email (form_data.username is standard field name for OAuth2 form)
    user = get_user_by_email(db, email=form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 2. Verify hashed password
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 3. Create JWT access token
    # We store the email in the 'sub' (subject) claim
    access_token = create_access_token(data={"sub": user.email})
    
    return {"access_token": access_token, "token_type": "bearer"}
