from pydantic import BaseModel, constr
from datetime import datetime
from typing import Optional

class CourseSchema(BaseModel):
    name: str
    description: str
    created_by_id: int

class CourseAuditSchema(CourseSchema):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]
    updated_by_id: Optional[CourseSchema]
    deleted_by_id: Optional[CourseSchema]