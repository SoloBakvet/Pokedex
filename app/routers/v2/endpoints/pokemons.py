from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination import paginate
from fastapi_pagination.links import Page

from app.crud import pokemon_crud
from app.db.database import SessionLocal, get_db
from app.schemas.pokemon.pokemon_schema import SimplePokemon


router = APIRouter(prefix="/pokemons",
    tags=["Pokemons"])

@router.get("/")
async def get_all_pokemons_paginated(sort: str | None = None, limit: int | None = None, offset: int | None = None, db: SessionLocal = Depends(get_db)) -> Page[SimplePokemon]:
    if sort:
        sorting_options = ["name-asc",
                           "name-desc",
                           "id-asc",
                           "id-desc"]
        if sort not in sorting_options:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    try:
        return paginate(pokemon_crud.query_pokemons(sort=sort, limit=limit, db=db))
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    