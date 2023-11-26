from fastapi import APIRouter, Depends
from configs.database import get_db
from services.auth_service import AuthService
from schemas.user_schema import UserWithTokenSchema
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=UserWithTokenSchema, status_code=200, summary="Login to the application with username and password")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    return AuthService(db).login(form_data)

