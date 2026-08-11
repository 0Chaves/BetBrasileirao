from pydantic import BaseModel, Field

from schemas.user_schema import UserResponse


class LoginRequest(BaseModel):
    # Aceita e-mail OU login no mesmo campo (o mockup do frontend usa um único campo "E-mail ou Usuário").
    login: str = Field(min_length=1, description="E-mail ou login do usuário")
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse
