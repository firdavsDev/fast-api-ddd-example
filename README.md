# 📝 FastAPI DDD ToDo API

A clean and scalable FastAPI project using **Domain-Driven Design (DDD)**.  
Includes JWT auth, SQLite, Docker, and metrics + pagination support.

---

## 🚀 Features

- 🧠 Domain-Driven Design
- 🔐 JWT Authentication
- ✅ User-specific ToDos
- 📊 Metrics endpoint (`/todos/stats`)
- 🔍 Search + pagination on todos
- 🐳 Docker support
- 🧪 Basic tests with `pytest`

---

## 📂 Project Structure (DDD)

```plaintext
.
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
```

## 🐳 Run with Docker

```bash
docker-compose up --build
```

Then visit: http://localhost:8000/docs
