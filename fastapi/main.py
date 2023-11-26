from fastapi import FastAPI
from configs.database import create_tables
from fastapi.middleware.cors import CORSMiddleware
from routers import user_router, auth_router

create_tables()

# CORS

origins = [ 'http://localhost:5173' ]

app = FastAPI()

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_methods=["*"], 
    allow_headers=["*"]
)

# Routers
app.include_router(user_router.router)
app.include_router(auth_router.router)






