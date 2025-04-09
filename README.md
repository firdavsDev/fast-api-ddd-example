# 📝 FastAPI DDD ToDo API

A clean and scalable FastAPI project using **Domain-Driven Design (DDD)**.  
Includes JWT auth, SQLite, Docker, and metrics + pagination support.

---

## 📂 Project Structure (DDD)

```plaintext
.
todo_app/
├── app/
│   ├── domain/                # Business logic
│   │   ├── models/            # Domain entities (e.g., ToDo, User)
│   │   └── repositories/      # Repository interfaces
│   ├── infrastructure/        # Database, external services
│   │   ├── db/                # SQLAlchemy models, DB setup
│   │   └── repositories/      # Repository implementations
│   ├── application/           # Use cases, DTOs
│   │   └── services/          # ToDo services (app logic)
│   ├── interfaces/            # Entry points (REST API)
│   │   └── routes/            # FastAPI routes
│   ├── core/                  # Configs, JWT utils, etc.
│   └── main.py                # FastAPI app entry
├── tests/                     # Unit/integration tests
├── requirements.txt
└── README.md

```

## 🐳 Run with Docker

```bash
docker-compose up --build
```

Then visit: http://localhost:8000/docs

🧪 Run Tests
```pytest```
