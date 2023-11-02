from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .audit_base import AuditBase

class GroupModel(AuditBase):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True)
    name = Column(String(55))
    time = Column(DateTime)
    course_id = Column(Integer, ForeignKey("course.id"))
    course = relationship("CourseModel", foreign_keys=[course_id])
