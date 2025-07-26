import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

# --- BẮT ĐẦU PHẦN CODE GỠ LỖI ---

# 1. Tải biến môi trường và in ra kết quả để xem nó có tìm thấy file .env không
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env') # Xác định đường dẫn tuyệt đối đến file .env
found_dotenv = load_dotenv(dotenv_path=dotenv_path)
print(f"DEBUG: Attempting to load .env from: {dotenv_path}")
print(f"DEBUG: Dotenv file found and loaded: {found_dotenv}")

# 2. Lấy biến DATABASE_URL và in ra giá trị của nó
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
print(f"DEBUG: Value of DATABASE_URL is: {SQLALCHEMY_DATABASE_URL}")

# --- KẾT THÚC PHẦN CODE GỠ LỖI ---


# Các dòng code còn lại giữ nguyên
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()