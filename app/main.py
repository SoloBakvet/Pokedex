from fastapi import FastAPI
from app.db import database
from app.schemas.external import external_helper
from app.routers.v1 import v1_api

database.Base.metadata.create_all(bind=database.engine)

external_helper.init_db()

app = FastAPI()
app.include_router(v1_api.router)