from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .audit_base import AuditBase

class AssistanceModel(AuditBase):
    __tablename__ = "assistance"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    student_id = Column(Integer, ForeignKey("student.id"))
    student = relationship("StudentModel", foreign_keys=[student_id])
    group_id = Column(Integer, ForeignKey("group.id"))
    group = relationship("GroupModel", foreign_keys=[group_id])