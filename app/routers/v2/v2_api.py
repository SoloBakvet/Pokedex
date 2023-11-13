from fastapi import APIRouter

from app.routers.v2.endpoints import pokemons

router = APIRouter(prefix="/api/v2")
router.include_router(pokemons.router)
