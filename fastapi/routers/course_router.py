from fastapi import APIRouter, Depends
from configs.database import get_db
from services.course_service import CourseService
from schemas.course_schema import CourseSchema, CourseCreateSchema
from utils.auth import get_current_user

router = APIRouter(
    prefix="/courses",
    tags=["courses"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[CourseSchema], summary="Get all courses")
async def get_all(db=Depends(get_db)):
    return CourseService(db).get_all() 

@router.get("/{id}", response_model=CourseSchema, summary="Get user by id")
async def get_by_id(id: int, db=Depends(get_db)):
    return CourseService(db).get_by_id(id)

@router.post("/", response_model=CourseSchema, status_code=201, summary="Create a new course")
async def create(obj_in: CourseCreateSchema, db=Depends(get_db)):
    return CourseService(db).create(obj_in, 1)

@router.put("/{id}", response_model=CourseSchema, summary="Update a course")
async def update(id: int, obj_in: CourseCreateSchema, db=Depends(get_db)):
    return CourseService(db).update(id, obj_in)

@router.delete("/{id}", response_model=bool, summary="Delete a course")
async def delete(id: int, db=Depends(get_db)):
    return CourseService(db).delete(id)