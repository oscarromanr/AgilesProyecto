from sqlalchemy import Column, String, Integer
from .audit_base import AuditBase

class TokenModel(AuditBase):
    __tablename__ = "token"

    id = Column(Integer, primary_key=True)
    token = Column(String(255))