from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from httpx2 import AsyncClient


async def test_get_2xx(client: AsyncClient) -> None:
    res = await client.get("/docs")
    assert 200 <= res.status_code <= 299


async def test_get_4xx(client: AsyncClient) -> None:
    res = await client.get("/never-gonna-give-you-up")
    assert res.status_code == 404
