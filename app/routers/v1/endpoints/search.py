from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse

router = APIRouter(prefix="/search",
    tags=["Search"])

@router.get("/")
async def searchForPokemons(sort : str | None = None):
    return HTMLResponse()

