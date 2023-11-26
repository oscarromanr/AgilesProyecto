from sqlalchemy.orm import Session
from repositories.user_repo import UserRepo
from models.user_model import UserModel
from schemas.user_schema import UserWithTokenSchema
from utils.app_exceptions import AppException
from utils.auth import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

class AuthService(object):

    def __init__(self, db: Session):
        self.db = db
        self.repo = UserRepo(UserModel, db)

    def login(self, credentials: UserWithTokenSchema):
        user = self.repo.login(credentials.username, credentials.password)
        if not user:
            raise AppException.Unauthorized(detail="Credenciales inválidas")
        access_token = create_access_token(data={"sub": user.username}, expires_delta=ACCESS_TOKEN_EXPIRE_MINUTES)
        return UserWithTokenSchema(user=user, token=access_token)