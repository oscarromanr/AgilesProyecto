from sqlalchemy import Column, String, Integer
from .audit_base import AuditBase

class UserModel(AuditBase):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, index=True)
    first_name = Column(String(55))
    last_name = Column(String(55))
    email = Column(String(255), unique=True)
    password = Column(String(255))