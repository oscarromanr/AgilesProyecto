from pydantic import BaseModel, constr
from datetime import datetime
from typing import Optional
from .user_schema import UserSchema

class LoginAttemptSchema(BaseModel):
    id: int

class CreateLoginAttemptSchema(BaseModel):
    created_by_id: int

class LoginAttemptAuditSchema(LoginAttemptSchema):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]
    created_by_id: Optional[UserSchema]
    updated_by_id: Optional[UserSchema]
    deleted_by_id: Optional[UserSchema]

    class Config:
        orm_mode=True