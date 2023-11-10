from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.db.database import SessionLocal, get_db
from app.db.manager import pokemon_details_list
from app.db import crud
from app.schemas import pokemon_schema


router = APIRouter(prefix="/pokemons",
    tags=["pokemons"])

@router.get("/", response_model=list[pokemon_schema.Pokemon])
async def get_all_pokemons(sort : str | None = None, db: SessionLocal = Depends(get_db)):
    if sort:
        sorting_options = {"name-asc" : True,
                           "name-desc" : True,
                           "id-asc" : True,
                           "id-desc" : True,
                           }
    items = crud.get_pokemons(db)
    return items

@router.get("/{id}")
async def get_pokemon_details():
    test = jsonable_encoder(pokemon_details_list)
    return JSONResponse(content=test)


        

@router.post("/", response_model=list[pokemon_schema.Pokemon])
def create_pokemon(pokemon: pokemon_schema.Pokemon, db: SessionLocal = Depends(get_db)):
   return crud.create_pokemon(db=db,pokemon=pokemon) 