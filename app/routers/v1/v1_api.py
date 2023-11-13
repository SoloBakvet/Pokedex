from fastapi import APIRouter

from app.routers.v1.endpoints import pokemons, teams, search

router = APIRouter(prefix="/api/v1")
router.include_router(pokemons.router)
router.include_router(teams.router)
router.include_router(search.router)


