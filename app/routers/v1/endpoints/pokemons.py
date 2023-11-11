from typing import List
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.db.database import SessionLocal, get_db
from app.crud import pokemon_crud
from app.schemas.pokemon.pokemon_schema import Pokemon, SimplePokemon

router = APIRouter(prefix="/pokemons",
    tags=["Pokemons"])

@router.get("/")
async def get_all_pokemons(sort: str | None = None, db: SessionLocal = Depends(get_db)) -> List[SimplePokemon]:
    if sort:
        sorting_options = {"name-asc" : True,
                           "name-desc" : True,
                           "id-asc" : True,
                           "id-desc" : True,
                           }
    items = pokemon_crud.query_pokemons(sort=sort, db=db)
    return items

@router.get("/{id}")
async def get_pokemon_by_id() -> Pokemon:
    #test = jsonable_encoder(pokemon_details_list)
    return JSONResponse()
