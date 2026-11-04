# 單元測試與格式化

!!! tips

    推薦在 pre-commit 或 CI/CD 自動化進行單元測試與格式化

## 安裝套件

使用命令

```bash
uv add inline-snapshot pytest pytest-asyncio pytest-cov pytest-dotenv pytest-mock time-machine --dev --raw
```

## 設定

在 `pyproject.toml` 加上

=== "pyproject.toml"

    ```toml
    # 其他設定...

    [tool.pytest.ini_options]
    addopts = [
        "-ra",
        "--tb=short",
        "--strict-markers",
        "--strict-config",
        "--durations=10",
        "--cov=.",
        "--cov-report=term-missing",
        "--cov-report=html",
    ]
    asyncio_mode = "auto"
    filterwarnings = [
        "error",
        "ignore::DeprecationWarning",
    ]
    pythonpath = "."
    testpaths = ["tests"]

    [tool.ruff]
    line-length = 88
    target-version = "py314"

    [tool.ruff.format]
    quote-style = "double"
    indent-style = "space"
    skip-magic-trailing-comma = false

    [tool.ruff.lint]
    select = [
        "ALL",
    ]
    ignore = [
        "CPY001",
        "D100",
        "D101",
        "D102",
        "D103",
        "D104",
        "D107",
        "D203",
        "D212",
        "D400",
        "D415",
        "E501",
        "PGH003",
        "PLR0913",
        "PLR0917",
        "RUF001",
        "RUF002",
        "RUF003",
    ]

    [tool.ruff.lint.flake8-type-checking]
    runtime-evaluated-base-classes = [
        "pydantic.BaseModel",
    ]
    runtime-evaluated-decorators = [
        "fastapi.FastAPI.delete",
        "fastapi.FastAPI.get",
        "fastapi.FastAPI.patch",
        "fastapi.FastAPI.post",
        "fastapi.FastAPI.put",
        "fastapi.APIRouter.delete",
        "fastapi.APIRouter.get",
        "fastapi.APIRouter.patch",
        "fastapi.APIRouter.post",
        "fastapi.APIRouter.put",
    ]

    [tool.ruff.lint.per-file-ignores]
    "tests/**/*.py" = [
        "INP001",
        "PLR2004",
        "S101",
        "S105",
        "S106",
    ]
    ```

## 格式化

使用命令

```bash
uv format

uvx ruff check
```

!!! tips

    若 `uvx ruff check` 有檢測出不符規範的地方時

    可視情況使用 `--fix` 與 `--unsafe-fixes` 參數

## 單元測試

建立 `tests` 資料夾並把單元測試檔案 `conftest.py` `test_xxx.py` 放入其中

然後使用命令

```bash
uv run pytest
```

!!! tips

    記得在 `.gitignore` 加上 `.coverage*`

### 測試 app

建立 `tests/conftest.py` `tests/test_app.py`

=== "tests/conftest.py"

    ```python
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
    ```

=== "tests/test_app.py"

    ```python
    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from httpx2 import AsyncClient


    async def test_get_2xx(client: AsyncClient) -> None:
        res = await client.get("/docs")
        assert 200 <= res.status_code <= 299


    async def test_get_4xx(client: AsyncClient) -> None:
        res = await client.get("/never-gonna-give-you-up")
        assert res.status_code == 404
    ```
