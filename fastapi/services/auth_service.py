from sqlalchemy.orm import Session
from repositories.user_repo import UserRepo
from models.user_model import UserModel
from schemas.user_schema import UserWithTokenSchema
from utils.app_exceptions import AppException
from utils.auth import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from .login_attempt_service import LoginAttemptService
from .user_service import UserService

class AuthService(object):

    def __init__(self, db: Session):
        self.db = db
        self.repo = UserRepo(UserModel, db)

    def login(self, credentials: UserWithTokenSchema):
        user = self.repo.login(credentials.username, credentials.password)
        if not user:
            user = self.repo.get_by_username(credentials.username)
            if user :
                login_attempts = LoginAttemptService(self.db).count_by_id(user.id)
                if login_attempts >= 5:
                    UserService(self.db).soft_delete(user.id)
                    raise AppException.Forbidden(detail="Se han detectado multiples intentos fallidos al iniciar sesion, para proteger tu usuario lo hemos bloqueado temporalmente, porfavor restablece tu contrasena")
                LoginAttemptService(self.db).create(user.id)
            raise AppException.Unauthorized(detail="Credenciales inválidas")
        if user.deleted_at:
            raise AppException.Forbidden(detail="Se han detectado multiples intentos fallidos al iniciar sesion, para proteger tu usuario lo hemos bloqueado temporalmente, porfavor restablece tu contrasena")
        access_token = create_access_token(data={"sub": user.username}, expires_delta=ACCESS_TOKEN_EXPIRE_MINUTES)
        return UserWithTokenSchema(user=user, token=access_token)