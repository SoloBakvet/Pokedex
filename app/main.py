from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.db import database
from app.routers.v1 import v1_api
from app.routers.v2 import v2_api

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Pokédex API",
    description="REST API built with FastAPI to manage Pokémon.",
    version="1.0.0"
)
app.include_router(v1_api.router)
app.include_router(v2_api.router)

add_pagination(app)
