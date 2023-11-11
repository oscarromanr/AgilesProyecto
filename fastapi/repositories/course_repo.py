from .base_repo import BaseRepo

class CourseRepo(BaseRepo):
    def get_by_name(self, name, id):
        return self.db.query(self.model).filter(self.model.name == name, self.model.created_by_id == id).first()