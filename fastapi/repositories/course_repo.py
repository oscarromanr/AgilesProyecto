from .base_repo import BaseRepo

class CourseRepo(BaseRepo):
    
    def get_by_user_id(self, user_id):
        return self.db.query(self.model).filter(self.model.user_id == user_id).all()