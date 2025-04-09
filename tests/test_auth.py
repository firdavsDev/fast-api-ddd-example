import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register_and_login():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as client:
        # Register
        res = await client.post(
            "/api/auth/register", json={"email": "user@test.com", "password": "123456"}
        )
        assert res.status_code == 200
        assert res.json()["email"] == "user@test.com"

        # Login
        res = await client.post(
            "/api/auth/login", json={"email": "user@test.com", "password": "123456"}
        )
        assert res.status_code == 200
        assert "access_token" in res.json()
