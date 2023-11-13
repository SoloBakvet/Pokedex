from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import NoResultFound, InvalidRequestError

from app.crud import team_crud
from app.db.database import SessionLocal, get_db
from app.schemas.team_schema import CreateTeamRequest, Team

router = APIRouter(prefix="/teams",
    tags=["Teams"])

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_teams(db: SessionLocal = Depends(get_db)) -> List[Team]:
    try:
        return team_crud.query_teams(db=db)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_team_by_id(id: int, db: SessionLocal = Depends(get_db)) -> Team:
    try:
        return team_crud.query_team(team_id=id, db=db)
    except NoResultFound:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Team not found.")
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_team(new_team: CreateTeamRequest, db: SessionLocal = Depends(get_db)) -> Team: 
    try:
        return team_crud.create_team(new_team=new_team, db=db)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@router.post("/{id}", status_code=status.HTTP_200_OK)
async def set_pokemons_of_team(pokemons: List[int], id: int, db: SessionLocal = Depends(get_db)) -> Team:
    try:
        return team_crud.update_pokemons_of_team(db=db, team_pokemons=pokemons, team_id=id)
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Team not found.")
    except InvalidRequestError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon in list not found.")
    