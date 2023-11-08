
from fastapi import FastAPI
from .routers.v1 import v1_api
from .db import manager

# TODO: Remove once database system is implemented
manager.init_db()

app = FastAPI()
app.include_router(v1_api.router)


