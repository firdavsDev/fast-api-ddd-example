from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.infrastructure.db.models import Base
from app.infrastructure.db.session import engine
from app.interfaces.routes import auth_routes, todo_routes

from .openapi import custom_openapi

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Todo API Domain Driven Design",
    description="A simple Todo API to demonstrate Domain Driven Design principles",
    version="0.1.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url=None,
    openapi_prefix="/api",
    openapi_tags=[
        {
            "name": "auth",
            "description": "Authentication and authorization routes",
        },
        {
            "name": "todos",
            "description": "Todo routes",
        },
    ],
)


# app.openapi = custom_openapi(app)

# CORS settings
origins = [
    "http://localhost:3000",
    "http://localhost:8000",
]

# middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# routers
app.include_router(todo_routes.router, prefix="/api/todos", tags=["todos"])
app.include_router(auth_routes.router, prefix="/api/auth", tags=["auth"])


@app.get("/")
async def root():
    return {"message": "Welcome to the Todo API!"}
