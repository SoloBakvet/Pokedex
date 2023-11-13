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
    return pokemon_crud.query_pokemons(sort=sort, db=db)

@router.get("/{id}")
async def get_pokemon_by_id(id : int, db: SessionLocal = Depends(get_db)) -> Pokemon:
    return pokemon_crud.query_pokemon(pokemon_id=id, db=db)
