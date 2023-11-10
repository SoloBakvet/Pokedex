from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from app.db.manager import pokemon_details_list

router = APIRouter(prefix="/teams",
    tags=["teams"])

@router.get("/")
async def get_all_teams(sort : str | None = None):
    return HTMLResponse()

@router.get("/{id}")
async def get_team():
    return HTMLResponse()

@router.post("/")
async def post_team(sort : str | None = None):
    return HTMLResponse()

@router.post("/{id}")
async def post_team_pokemons():
    return HTMLResponse()