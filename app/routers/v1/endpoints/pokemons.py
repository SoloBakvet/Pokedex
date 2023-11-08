from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.db.manager import pokemon_details_list

router = APIRouter(prefix="/pokemons",
    tags=["pokemons"])

@router.get("/")
async def getAllPokemons(sort : str | None = None):
    if sort:
        sorting_options = {"name-asc" : True,
                           "name-desc" : True,
                           "id-asc" : True,
                           "id-desc" : True,
                           }
    test = jsonable_encoder(pokemon_details_list)
    return JSONResponse(content=test)

@router.get("/{id}")
async def getPokemon():
    test = jsonable_encoder(pokemon_details_list)
    return JSONResponse(content=test)