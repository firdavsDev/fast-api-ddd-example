import pytest
from httpx import AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_register_and_login():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Register
        res = await client.post(
            "/register", json={"email": "user@test.com", "password": "123456"}
        )
        assert res.status_code == 200
        assert res.json()["email"] == "user@test.com"

        # Login
        res = await client.post(
            "/login", json={"email": "user@test.com", "password": "123456"}
        )
        assert res.status_code == 200
        assert "access_token" in res.json()
