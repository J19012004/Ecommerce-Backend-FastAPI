# Ecommerce Backend System (FastAPI)

A scalable and secure backend system for an ecommerce application built using **FastAPI** and **PostgreSQL**. The project implements authentication, product management, cart functionality, and order processing with a clean modular architecture.

---


## Project Screenshots

<img width="1280" height="684" alt="1780998253709" src="https://github.com/user-attachments/assets/887df5bf-a6eb-414a-a987-04faffd57aa7" />

<img width="1280" height="678" alt="1780998253745" src="https://github.com/user-attachments/assets/d43ef5c7-e6ef-4362-af52-ede03c021f1a" />

<img width="1280" height="656" alt="1780998253387" src="https://github.com/user-attachments/assets/5e1951e7-6083-4c27-8f02-f1c8779f2a22" />





---

## Features

- Secure user authentication using JWT
- Product and category management (CRUD APIs)
- Shopping cart system for users
- Order placement and order history tracking
- Protected routes with authorization
- Relational database design with SQLAlchemy Async ORM
- RESTful API architecture
- Interactive API documentation using Swagger / OpenAPI

---

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy (Async ORM)
- JWT Authentication
- Pydantic
- Swagger / OpenAPI
- Git & GitHub

---

## Project Structure

```
app/
├── api/
│   └── v1/
│       └── endpoints/
│           ├── auth.py
│           ├── products.py
│           ├── categories.py
│           ├── cart.py
│           └── orders.py
├── core/
│   ├── config.py
│   ├── database.py
│   └── security.py
├── models/
├── schemas/
└── main.py
```

---

## API Modules

- **Authentication** — Register, Login, JWT token generation
- **Products** — Create, Read, Update, Delete products
- **Categories** — Manage product categories
- **Cart** — Add/remove items, view cart
- **Orders** — Place orders, view order history

---

## Authentication Flow

1. Register → `POST /auth/register`
2. Login → `POST /auth/login` → receive JWT token
3. Click **Authorize** in Swagger UI
4. Paste token to access protected endpoints

---

## Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/J19012004/Ecommerce-Backend-FastAPI.git
cd Ecommerce-Backend-FastAPI
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:
```env
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_DB=your_db_name
POSTGRES_HOST=your_db_host
POSTGRES_PORT=5432
JWT_SECRET_KEY=your_secret_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REDIS_URL=redis://localhost:6379
```

### 5. Run the application
```bash
uvicorn app.main:app --reload
```

### 6. Access Swagger UI
```
http://127.0.0.1:8000/docs
```

---

## Live Demo

The API is deployed on Render and accessible at:

👉 **https://ecommerce-backend-fastapi-kula.onrender.com/docs**
Note: Free instance may take ~50 seconds to wake up on first request.


---

## Author

**Jerminn Rebekka M**  
GitHub: [@J19012004](https://github.com/J19012004)

