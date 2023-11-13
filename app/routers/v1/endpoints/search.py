from typing import List
from fastapi import APIRouter, Depends, HTTPException, status

from app.crud import pokemon_crud
from app.db.database import SessionLocal, get_db
from app.schemas.pokemon.pokemon_schema import SimplePokemon

router = APIRouter(prefix="/search",
    tags=["Search"])

@router.get("/", status_code=status.HTTP_200_OK)
async def search_for_pokemons(query: str, limit: int | None = None,  db: SessionLocal = Depends(get_db)) -> List[SimplePokemon]:
    if (len(query) == 0):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    try:
        return pokemon_crud.advanced_pokemon_query(query=query, limit=limit, db=db)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
