from fastapi import FastAPI

app = FastAPI()

app.frontend("/site", directory="site")
