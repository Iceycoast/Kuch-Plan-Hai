# Kuch Plan Hai - Backend

A FastAPI backend application for the "Kuch Plan Hai" project, providing REST API endpoints for user authentication and activity planning.

## Features

- 🔐 JWT Authentication
- 👤 User Management (Registration, Login)
- 🗄️ PostgreSQL Database with SQLAlchemy ORM
- 📊 Database Migrations with Alembic
- 🔒 Password Hashing with bcrypt
- 📝 Pydantic Data Validation
- 🚀 FastAPI with automatic API documentation

## Tech Stack

- **FastAPI** - Modern, fast web framework
- **PostgreSQL** - Relational database
- **SQLAlchemy** - Python SQL toolkit and ORM
- **Alembic** - Database migration tool
- **Pydantic** - Data validation using Python type hints
- **bcrypt** - Password hashing
- **python-jose** - JWT token handling
- **python-multipart** - Form data handling

## Getting Started

### Prerequisites

- Python 3.8 or higher
- PostgreSQL database
- pip (Python package installer)

### Installation

1. Clone the repository and navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables:
   Create a `.env` file in the backend directory:
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/kuch_plan_hai
   SECRET_KEY=your-secret-key-here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

6. Set up the database:
   ```bash
   # Run database migrations
   alembic upgrade head
   ```

7. Start the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`

### API Documentation

Once the server is running, you can access:
- **Interactive API docs**: `http://localhost:8000/docs`
- **ReDoc documentation**: `http://localhost:8000/redoc`

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── config.py            # Configuration settings
│   ├── db.py               # Database connection
│   ├── auth/               # Authentication module
│   │   ├── routes.py       # Auth endpoints
│   │   └── utils.py        # Auth utilities
│   ├── controllers/        # Business logic
│   │   └── auth_controller.py
│   ├── models/             # SQLAlchemy models
│   │   └── user.py
│   └── schemas/            # Pydantic schemas
│       └── auth.py
├── alembic/                # Database migrations
├── requirements.txt        # Python dependencies
└── schema.sql             # Database schema
```

## Available Endpoints

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `POST /auth/logout` - User logout (planned)

### Health Check
- `GET /health` - API health status

## Database Schema

The application uses the following main tables:
- **users** - User account information
  - id (Primary Key)
  - email (Unique)
  - first_name
  - last_name
  - hashed_password
  - created_at
  - updated_at

## Development

### Running Tests
```bash
# Run tests (when implemented)
pytest
```

### Database Migrations
```bash
# Create a new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

### Code Quality
```bash
# Format code with black
black .

# Sort imports with isort
isort .

# Lint with flake8
flake8 .
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | Required |
| `SECRET_KEY` | Secret key for JWT tokens | Required |
| `ALGORITHM` | JWT algorithm | HS256 |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiration time | 30 |

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request
