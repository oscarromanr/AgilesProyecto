from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from .audit_base import AuditBase

class CourseModel(AuditBase):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True)
    name = Column(String(55))
    description = Column(String(255))
    groups = relationship("GroupModel", back_populates="course")