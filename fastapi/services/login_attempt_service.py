from sqlalchemy.orm import Session
from repositories.login_attempt_repo import LoginAttemptRepo
from models.login_attempt_model import LoginAttemptModel
from schemas.login_attempt_schema import CreateLoginAttemptSchema
from utils.app_exceptions import AppException
from utils.auth import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

class LoginAttemptService(object):

    def __init__(self, db: Session):
        self.db = db
        self.repo = LoginAttemptRepo(LoginAttemptModel, db)

    def create(self, user_id):
        login_attempt = CreateLoginAttemptSchema(created_by_id = user_id)
        return self.repo.create(login_attempt)
    
    def count_by_id(self, user_id):
        return self.repo.count_by_id(user_id)