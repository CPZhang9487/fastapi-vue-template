# 建立基本 FastAPI 應用

## 建立開發環境

使用命令

```bash
# 建立專案
uv init --no-package your-app-name

cd your-app-name

# 添加 module
uv add fastapi[all] --raw
```

## 編寫程式

建立 `app.py`

```python title="app.py"
from fastapi import FastAPI

app = FastAPI()
```

## 運行

使用命令運行

```bash
# 熱更新開發模式
uv run fastapi dev
```

此時會看到終端顯示

```bash
 ⚡️ Starting FastAPI in development mode

 🐍 Using import string: app:app (auto-discovered, use --verbose to learn more)

 💡 You can configure an entrypoint in pyproject.toml for this app with:

    [tool.fastapi]
    entrypoint = "app:app"

 🌐 Server started at http://127.0.0.1:8000
    Documentation at http://127.0.0.1:8000/docs

  Logs:

 ▕  Will watch for changes in these directories: ['/home/usr/fastapi-vue-template']
 ▕  Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
 ▕  Started reloader process [19016] using WatchFiles
 ▕  Started server process [16868]
 ▕  Waiting for application startup.
 ▕  Application startup complete.
```

## 細節補全

從剛剛終端的輸出可以看到

```bash hl_lines="3-8"
 ⚡️ Starting FastAPI in development mode

 🐍 Using import string: app:app (auto-discovered, use --verbose to learn more)

 💡 You can configure an entrypoint in pyproject.toml for this app with:

    [tool.fastapi]
    entrypoint = "app:app"

 🌐 Server started at http://127.0.0.1:8000
    Documentation at http://127.0.0.1:8000/docs

  Logs:

 ▕  Will watch for changes in these directories: ['/home/usr/fastapi-vue-template']
 ▕  Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
 ▕  Started reloader process [19016] using WatchFiles
 ▕  Started server process [16868]
 ▕  Waiting for application startup.
 ▕  Application startup complete.
```

可以看到推薦設定 `pyproject.toml`

```toml title="pyproject.toml"
# 其他設定...

[tool.fastapi]
entrypoint = "app:app"
```

再次運行會看到終端輸出

```bash
 ⚡️ Starting FastAPI in development mode

 🐍 Using import string: app:app

 🌐 Server started at http://127.0.0.1:8000
    Documentation at http://127.0.0.1:8000/docs

  Logs:

 ▕  Will watch for changes in these directories: ['/home/usr/fastapi-vue-template']
 ▕  Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
 ▕  Started reloader process [23784] using WatchFiles
 ▕  Started server process [15848]
 ▕  Waiting for application startup.
 ▕  Application startup complete.
```

## 瀏覽

```bash hl_lines="1-2"
 🌐 Server started at http://127.0.0.1:8000
    Documentation at http://127.0.0.1:8000/docs
```

從終端輸出可以看到提示瀏覽 <http://127.0.0.1:8000> 與 <http://127.0.0.1:8000/docs>

進行瀏覽後會看到終端輸出

```bash
 ▕  127.0.0.1:56874 - "GET / HTTP/1.1" 404
 ▕  127.0.0.1:56874 - "GET /docs HTTP/1.1" 200
 ▕  127.0.0.1:56874 - "GET /openapi.json HTTP/1.1" 200
```

稍微解析一下

- `127.0.0.1:56874`: 來源
- `GET`: HTTP method
- `/`: uri
- `HTTP/1.1`: HTTP 版本
- `404`: 回應狀態碼
