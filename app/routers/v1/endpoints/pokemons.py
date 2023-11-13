from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import NoResultFound

from app.db.database import SessionLocal, get_db
from app.crud import pokemon_crud
from app.schemas.pokemon.pokemon_schema import Pokemon, SimplePokemon

router = APIRouter(prefix="/pokemons",
    tags=["Pokemons"])

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_pokemons(sort: str | None = None, db: SessionLocal = Depends(get_db)) -> List[SimplePokemon]:
    if sort:
        sorting_options = ["name-asc",
                           "name-desc",
                           "id-asc",
                           "id-desc"]
        if sort not in sorting_options:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
            
    try:
        return pokemon_crud.query_pokemons(sort=sort, db=db)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_pokemon_by_id(id: int, db: SessionLocal = Depends(get_db)) -> Pokemon:
    try:
        return pokemon_crud.query_pokemon(pokemon_id=id, db=db)
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon not found.")
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    