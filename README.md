# Basic CRUD App Using FastAPI

A lightweight RESTful API built with FastAPI that demonstrates fundamental CRUD (Create, Read, Update, Delete) operations. This project serves as a learning resource and starter template for building scalable APIs with Python's modern async framework.

## 🚀 Features

- **FastAPI Framework** - Modern, high-performance web framework for building APIs with Python 3.7+
- **Automatic API Documentation** - Interactive Swagger UI at `/docs` and ReDoc at `/redoc`
- **CRUD Operations** - Complete Create, Read, Update, Delete functionality
- **Data Validation** - Built-in request/response validation using Pydantic models
- **SQLAlchemy Integration** - ORM for database operations (if database is configured)
- **Type Hints** - Full type annotation for better code quality and IDE support

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Virtual environment tool (venv, virtualenv, or conda)

## 🔧 Installation

1. **Clone the repository**
```bash
git clone https://github.com/AnuragSingh1104/Basic-CRUD-app-Using-Fast-API.git
cd Basic-CRUD-app-Using-Fast-API
```

2. **Create a virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present, install core dependencies manually:
```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

## 📁 Project Structure

```
Basic-CRUD-app-Using-Fast-API/
│
├── main.py              # Main application file with API routes
├── models.py            # SQLAlchemy database models
├── schemas.py           # Pydantic models for request/response validation
├── database.py          # Database connection and session configuration
├── crud.py              # CRUD operation functions
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## 🔌 API Endpoints

### Items Resource

| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| `GET` | `/employees_read` | Retrieve all employees | - |
| `GET` | `/employees/{employees_id}` | Get specific item by ID | - |
| `POST` | `/employees` | Create a new item | `{"name": "string", "description": "string"}` |
| `PUT` | `/employees/{employees_id}` | Update an existing item | `{"name": "string", "description": "string"}` |
| `DELETE` | `/employees/{employees_id}` | Delete an item | - |

## 💡 Usage Examples

### Create an Item
```bash
curl -X POST "http://127.0.0.1:8000/items" \
  -H "Content-Type: application/json" \
  -d '{"name": "Sample Item", "description": "This is a test item"}'
```

### Get All Items
```bash
curl -X GET "http://127.0.0.1:8000/items"
```

### Get Single Item
```bash
curl -X GET "http://127.0.0.1:8000/items/1"
```

### Update an Item
```bash
curl -X PUT "http://127.0.0.1:8000/items/1" \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Item", "description": "Updated description"}'
```

### Delete an Item
```bash
curl -X DELETE "http://127.0.0.1:8000/items/1"
```

## 🗄️ Database Configuration

The application can use either:
- **SQLite** (default) - Lightweight file-based database for development
- **PostgreSQL** - Production-ready relational database
- **MySQL** - Alternative relational database option

### SQLite Configuration (Default)
```python
# database.py
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
```

### PostgreSQL Configuration
```python
# database.py
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"
```

## 🧪 Testing

Test the API using the built-in Swagger UI at `/docs` or use tools like:
- **Postman** - GUI-based API testing
- **curl** - Command-line HTTP client
- **HTTPie** - User-friendly command-line HTTP client
- **pytest** - For automated testing (if test suite is implemented)

## 🛠️ Technologies Used

- **[FastAPI](https://fastapi.tiangolo.com/)** - Web framework for building APIs
- **[Uvicorn](https://www.uvicorn.org/)** - ASGI server for running FastAPI
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** - Data validation using Python type hints
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - SQL toolkit and ORM
- **[Starlette](https://www.starlette.io/)** - ASGI framework (FastAPI is built on top of it)

