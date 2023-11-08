from fastapi import APIRouter

from app.routers.v1.endpoints import pokemons

router = APIRouter(prefix="/api/v1",
    tags=["v1"])

router.include_router(pokemons.router)


