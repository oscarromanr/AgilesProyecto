from pydantic import BaseModel, constr
from datetime import datetime
from typing import Optional

class UserCredentialsSchema(BaseModel):
    username: str
    password: str

class UserCreateSchema(UserCredentialsSchema):
    first_name: str
    last_name: str
    email: constr(regex=r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$")

class UserSchema(UserCreateSchema):
    id: int

    class Config:
        orm_mode = True

class UserWithouthPasswordSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: constr(regex=r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$")

    class Config:
        orm_mode = True

class UserWithTokenSchema(BaseModel):
    user: UserWithouthPasswordSchema
    token: str

class UserAudit(UserWithouthPasswordSchema):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]
    created_by_id: Optional[UserSchema]
    updated_by_id: Optional[UserSchema]
    deleted_by_id: Optional[UserSchema]