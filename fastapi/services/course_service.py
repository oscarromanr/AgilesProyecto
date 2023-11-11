from sqlalchemy.orm import Session
from repositories.course_repo import CourseRepo 
from models.course_model import CourseModel
from schemas.course_schema import CourseSchema
from utils.app_exceptions import AppException

class CourseService(object):
    def __init__(self, db: Session):
        self.db = db
        self.repo = CourseRepo(CourseModel, db)

    def create(self, obj_in: CourseSchema):
        course = self.repo.get_by_name(obj_in.name, obj_in.created_by_id)
        if course:
            raise AppException.Conflict(detail=f"El usuario ya tiene un curso con ese nombre: {obj_in.name}")
        return self.repo.create(obj_in).__dict__

    def get_all(self):
            return self.repo.get_all()