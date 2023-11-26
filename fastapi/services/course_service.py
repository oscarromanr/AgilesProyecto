from sqlalchemy.orm import Session
from repositories.course_repo import CourseRepo
from models.course_model import CourseModel
from schemas.course_schema import CourseCreateSchema
from utils.app_exceptions import AppException

class CourseService(object):

    def __init__(self, db: Session):
        self.db = db
        self.repo = CourseRepo(CourseModel, db)

    def get_all(self):
        return self.repo.get_all()
    
    def get_by_id(self, id: int):
        course = self.repo.get_by_id(id)
        if not course:
            raise AppException.NotFound(detail=f"No se ha encontrado el curso con el id: {id}")
        return course
    
    def create(self, obj_in: CourseCreateSchema, user_id: str):
        print(user_id)
        obj_in.created_by_id = user_id
        return self.repo.create(obj_in)
    
    def update(self, id: int, obj_in):
        course = self.repo.get_by_id(id)
        if not course:
            raise AppException.NotFound(detail=f"No se ha encontrado el curso con el id: {id}")
        return self.repo.update(course, obj_in)
    
    def delete(self, id: int):
        course = self.repo.get_by_id(id)
        if not course:
            raise AppException.NotFound(detail=f"No se ha encontrado el curso con el id: {id}")
        return self.repo.delete(id)
    
    def soft_delete(self, id: int):
        course = self.repo.get_by_id(id)
        if not course:
            raise AppException.NotFound(detail=f"No se ha encontrado el curso con el id: {id}")
        return self.repo.soft_delete(course)