from pydantic import BaseModel, constr
from datetime import datetime
from typing import Optional

class CourseCreateSchema(BaseModel):
    name: str
    description: str
    created_by_id: Optional[int]

    class Config:
        #Do not show the created_by_id in the documentation
        schema_extra = {
            "example": {
                "name": "Curso de Python",
                "description": "Curso de Python para principiantes",
            }
        }

class CourseSchema(CourseCreateSchema):
    id: int

    class Config:
        orm_mode = True

class CourseAuditSchema():
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]
    created_by_id: Optional[int]
    updated_by_id: Optional[int]
    deleted_by_id: Optional[int]