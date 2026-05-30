# 🛒 Ecommerce Backend System (FastAPI)

A scalable and secure backend system for an ecommerce application built using FastAPI and PostgreSQL.  
The project implements authentication, product management, cart functionality, and order processing with a modular backend architecture.

---

## 🚀 Features

- Secure user authentication using JWT
- Product and category management (CRUD APIs)
- Shopping cart system for users
- Order placement and order history tracking
- Protected routes with authorization
- Relational database design with SQLAlchemy ORM
- RESTful API architecture
- Interactive API documentation using Swagger/OpenAPI

---

## 🛠 Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy (Async ORM)
- JWT Authentication
- Pydantic
- Swagger / OpenAPI
- Git & GitHub

---

## 🧱 System Architecture
Authentication → Products → Categories → Cart → Orders

---

## 📁 Project Structure
app/
├── api/
│ └── v1/endpoints/
├── core/
├── models/
├── schemas/
└── main.py

---

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone https://github.com/J19012004/ecommerce-api.git
cd ecommerce-api


### 2. Create virtual environment

python -m venv venv
venv\Scripts\activate  

### 3. Install dependencies
pip install -r requirements.txt

### 4. Configure environment variables

 DATABASE_URL=your_database_url
JWT_SECRET_KEY=your_secret_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

 ### 5.Run the application
uvicorn app.main:app --reload

---

## 📌 API Documentation
After running the server, access Swagger UI:

http://127.0.0.1:8000/docs

---

## 🔐 Authentication Flow
1.Register user → /auth/register
2.Login user → /auth/login
3.Copy JWT token
4.Click Authorize in Swagger UI
5.Access protected endpoints

---

## 📦 Modules
-Authentication Module (JWT)
-Product Management
-Category Management
-Cart System
-Order Management

---

## 📊 Project Highlights
-Built modular backend architecture using FastAPI
-Implemented secure JWT-based authentication system
-Designed relational database schema using SQLAlchemy ORM
-Developed full ecommerce workflow from product to order
-Integrated Swagger/OpenAPI for API testing and documentation

---

## Author
Jerminn Rebekka M
GitHub: https://github.com/J19012004

---

## 📌 Future Improvements
-Redis caching for performance optimization
-Docker containerization
-CI/CD pipeline with GitHub Actions


