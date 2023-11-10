from fastapi import FastAPI

from app.db import database
from app.routers.v1 import v1_api

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(v1_api.router)