from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound,InvalidRequestError
from app.models.pokemon_model import PokemonDBModel
from app.models.team_model import TeamDBModel
from app.schemas.team_schema import NewTeamRequest, Team

def convert_team_from_db(db_team: TeamDBModel) -> Team:
    converted_team = Team.model_validate(db_team)
    for db_pokemon in db_team.team_pokemons:
        converted_team.pokemons.append(db_pokemon.id)
    return converted_team
    
def query_teams(db: Session) -> List[Team]:
    db_teams = db.query(TeamDBModel).all()
    teams = list()
    for db_team in db_teams:
        teams.append(convert_team_from_db(db_team))
    return teams

def query_team(team_id: int, db: Session) -> Team:
    db_team = db.query(TeamDBModel).filter_by(id=team_id).first()
    if(db_team is None):
        raise NoResultFound
    return convert_team_from_db(db_team)

def create_team(new_team: NewTeamRequest, db: Session) -> Team:
    db.add(TeamDBModel(name=new_team.name))
    db.commit()
    db_team = db.query(TeamDBModel).filter_by(name=new_team.name).first()
    return db_team
    
def update_pokemons_of_team(team_id: int, team_pokemons: List[int], db:Session) -> Team:
    db_team = db.query(TeamDBModel).filter_by(id=team_id).first()
    db_pokemons = db.query(PokemonDBModel).filter(PokemonDBModel.id.in_(team_pokemons)).all()
    if(len(db_pokemons) != len(team_pokemons)):
        raise InvalidRequestError
    for db_pokemon in db_team.team_pokemons:
        db_team.team_pokemons.remove(db_pokemon)
    for db_pokemon in db_pokemons:
        db_team.team_pokemons.append(db_pokemon)
    db.commit()
    return convert_team_from_db(db_team)