
# 🧮 Math Microservice – FastAPI

This project is an asynchronous microservice built with FastAPI, offering a RESTful API for solving three fundamental math operations:

- Exponentiation (`pow`)
- Fibonacci number (`fibonacci`)
- Factorial (`factorial`)

The application is designed with microservice architecture principles in mind and follows a clean, scalable **MVC structure** (Model - View - Controller). All API requests are persisted in a local SQLite database using `aiosqlite`, allowing retrieval of historical computations.

---

## 📦 Project Structure

```
math_microservice/
├── main.py                     # Application entry point and router mounting
├── controllers/
│   └── math_controller.py      # All API endpoints
├── services/
│   └── math_service.py         # Business logic: request persistence
├── models/
│   ├── schemas.py              # Pydantic models for input/output validation
│   └── database.py             # init_db() function and SQLite connection
├── utils/
│   └── response.py             # Standard response function (api_response)
└── requests.db                 # Local database (auto-generated)
```

---

## ▶️ How to Run the Application

1. (Optional) Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate        # Mac/Linux
.venv\Scripts\activate         # Windows
```

2. Install all dependencies:
```bash
pip install -r requirements.txt
```

3. Launch the FastAPI server:
```bash
uvicorn main:app --reload
```

Then open your browser and go to:
```
http://127.0.0.1:8000/docs
```

This will open the interactive Swagger UI where you can test all endpoints.

---

## 🧪 API Testing

### Available Endpoints:

| Method | Path                         | Description                            |
|--------|------------------------------|----------------------------------------|
| GET    | `/`                          | Welcome message                        |
| POST   | `/api/pow`                   | Calculates `a^b`                       |
| POST   | `/api/fibonacci`             | Returns the n-th Fibonacci number      |
| POST   | `/api/factorial`             | Computes factorial of n                |
| GET    | `/api/logs`                  | Returns all saved requests             |
| GET    | `/api/logs?operation=pow`    | Filters logs by operation type         |

---

## ✅ Response Format

All endpoints return a standardized JSON response using the `api_response()` wrapper:
```json
{
  "status": "ok",
  "message": "Success",
  "data": {
    "result": 24
  }
}
```

In case of error:
```json
{
  "status": "error",
  "message": "n must be non-negative",
  "data": null
}
```

---

## 🧠 Modular Architecture (MVC)

The project follows a clean separation of concerns using the MVC pattern:

- **Models** (`models/`): 
  - Pydantic validation schemas (`PowRequest`, `LogEntry`, etc.)
  - Database connection and setup
- **Controllers** (`controllers/`): Handle API routes
- **Services** (`services/`): Contains business logic (e.g., saving logs)
- **Utils** (`utils/`): Shared utilities like standardized responses

This structure makes the project easy to extend (e.g., adding more math operations) and maintain.

---

## 📌 Final Notes

- Code is `flake8` and PEP8 compliant
- Designed to be lightweight and modular
- No Docker or external services required
- Database is auto-created on first run
