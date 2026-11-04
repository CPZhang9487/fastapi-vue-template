from typing import TYPE_CHECKING

import pytest
from httpx2 import ASGITransport, AsyncClient

from app import app

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator


@pytest.fixture
async def client() -> AsyncGenerator[AsyncClient]:
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport) as client:
        yield client
