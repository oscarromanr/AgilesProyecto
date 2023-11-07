from .base_repo import BaseRepo

class LoginAttemptRepo(BaseRepo):
    
    def count_by_id(self, id):
        return self.db.query(self.model).filter(self.model.created_by_id == id).count()