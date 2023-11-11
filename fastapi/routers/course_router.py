from fastapi import APIRouter, Depends
from configs.database import get_db
from services.course_service import CourseService
from schemas.course_schema import CourseSchema
from utils.auth import get_current_user

router = APIRouter(
    prefix="/courses",
    tags=["courses"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=CourseSchema, status_code=201, summary="Create a new course")
async def create(obj_in: CourseSchema, db=Depends(get_db)):
    return CourseService(db).create(obj_in)

@router.get("/", response_model=list[CourseSchema], summary="Get all courses")
async def get_all(db=Depends(get_db), current_user: str = Depends(get_current_user)):
    return CourseService(db).get_all() 
