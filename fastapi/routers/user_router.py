from fastapi import APIRouter, Depends
from configs.database import get_db
from services.user_service import UserService
from schemas.user_schema import UserWithouthPasswordSchema, UserCreateSchema
from utils.auth import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[UserWithouthPasswordSchema], summary="Get all users")
async def get_all(db=Depends(get_db), current_user: str = Depends(get_current_user)):
    return UserService(db).get_all() 

@router.get("/{id}", response_model=UserWithouthPasswordSchema, summary="Get user by id")
async def get_by_id(id: int, db=Depends(get_db), current_user: str = Depends(get_current_user)):
    return UserService(db).get_by_id(id)

@router.post("/", response_model=UserWithouthPasswordSchema, status_code=201, summary="Create a new user")
async def create(obj_in: UserCreateSchema, db=Depends(get_db)):
    return UserService(db).create(obj_in)

@router.put("/{id}", response_model=UserWithouthPasswordSchema, summary="Update a user")
async def update(id: int, obj_in: UserCreateSchema, db=Depends(get_db), current_user: str = Depends(get_current_user)):
    return UserService(db).update(id, obj_in)

@router.delete("/{id}", response_model=bool, summary="Delete a user")
async def delete(id: int, db=Depends(get_db), current_user: str = Depends(get_current_user)):
    return UserService(db).delete(id)
