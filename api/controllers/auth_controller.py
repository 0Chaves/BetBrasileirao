from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.orm import Session
from core.dependencies import get_db
from core.security import verify_password, create_access_token
from repositories.user_repository import user_repository
import schemas.auth_schema as schema
import schemas.user_schema as user_schema

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/login", response_model=schema.TokenResponse)
def login(credentials: schema.LoginRequest, db: Session = Depends(get_db)):
    user = user_repository.find_by_identifier(db, credentials.login)

    if not user or not verify_password(credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail/usuário ou senha inválidos",
        )

    if not user.isActive:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Esta conta está desativada",
        )

    token = create_access_token(subject=str(user.id), extra_claims={"isAdmin": user.isAdmin})
    return schema.TokenResponse(
        access_token=token,
        user=user_schema.UserResponse.model_validate(user),
    )