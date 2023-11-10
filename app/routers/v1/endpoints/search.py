from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from app.db.manager import pokemon_details_list

router = APIRouter(prefix="/search",
    tags=["search"])

@router.get("/")
async def searchForPokemons(sort : str | None = None):
    return HTMLResponse()

