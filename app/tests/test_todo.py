import pytest
from httpx import AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_create_and_get_todo():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Register + Login
        await client.post(
            "/register", json={"email": "todo@test.com", "password": "pass123"}
        )
        res = await client.post(
            "/login", json={"email": "todo@test.com", "password": "pass123"}
        )
        token = res.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        # Create ToDo
        res = await client.post("/todos", json={"title": "Test ToDo"}, headers=headers)
        assert res.status_code == 200
        assert res.json()["title"] == "Test ToDo"

        # Get Todos
        res = await client.get("/todos", headers=headers)
        assert res.status_code == 200
        assert len(res.json()) > 0
