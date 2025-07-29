from fastapi.middleware.cors import CORSMiddleware
from .api.v1 import pools as pools_router
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from . import crud, models, schemas, security
from .database import SessionLocal, engine

# Tạo các bảng trong database
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Swim360 API")
# Cấu hình CORS
origins = [
     "http://localhost:5173",
    "http://127.0.0.1:5173",
    # Thêm IP của bạn vào đây
    "172.20.10.2:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Dependency để lấy database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/login", response_model=schemas.Token)
def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = crud.get_user_by_email(db, email=form_data.username)
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = security.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/register", response_model=schemas.User)
def create_user_endpoint(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return crud.create_user(db=db, user=user)
app.include_router(pools_router.router, prefix="/pools", tags=["Pools"])
@app.get("/")
def read_root():
    return {"message": "Welcome to Swim360 API!"}