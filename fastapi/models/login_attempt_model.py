from sqlalchemy import Column, String, Integer
from .audit_base import AuditBase

class LoginAttemptModel(AuditBase):
    __tablename__ = "login_attempt"

    id = Column(Integer, primary_key=True)