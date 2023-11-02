from sqlalchemy import Column, String, Integer
from .audit_base import AuditBase

class StudentModel(AuditBase):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(55))
    last_name = Column(String(55))