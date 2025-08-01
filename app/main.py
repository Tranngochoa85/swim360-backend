from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .api.v1 import admin as admin_router
from .api.v1 import pools as pools_router
from .api.v1 import bookings as bookings_router
from .api.v1 import auth as auth_router

# Tạo các bảng trong database
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Swim360 API")

# Cấu hình CORS
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://172.20.10.2:5173", # IP mạng của bạn
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Kết nối các router
app.include_router(auth_router.router, prefix="/auth", tags=["Auth"]) # Đổi /login, /register thành /auth/login, /auth/register
app.include_router(pools_router.router, prefix="/pools", tags=["Pools"])
app.include_router(bookings_router.router, prefix="/bookings", tags=["Bookings"])
app.include_router(admin_router.router, prefix="/admin", tags=["Admin"])


@app.get("/")
def read_root():
    return {"message": "Welcome to Swim360 API!"}