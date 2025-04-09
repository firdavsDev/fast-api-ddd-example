import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_and_get_todo():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as client:
        # Register + Login
        await client.post(
            "/api/auth/register", json={"email": "todo@test.com", "password": "pass123"}
        )
        res = await client.post(
            "/api/auth/login", json={"email": "todo@test.com", "password": "pass123"}
        )
        token = res.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        # Create ToDo
        res = await client.post(
            "/api/todos/create", json={"title": "Test ToDo"}, headers=headers
        )
        assert res.status_code == 200
        assert res.json()["title"] == "Test ToDo"

        # Get Todos
        res = await client.get("/api/todos/list", headers=headers)
        assert res.status_code == 200
        assert len(res.json()) > 0
