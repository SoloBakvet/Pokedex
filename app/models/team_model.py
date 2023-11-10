from typing import List
from sqlalchemy import Column, ForeignKey, Integer, String, Table, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from app.db.database import Base
from app.models.pokemon_model import PokemonDBModel

team_pokemon_association_table = Table(
    "team_pokemon_association_table",
    Base.metadata,
    Column("team_id", ForeignKey("teams.id")),
    Column("pokemon_id", ForeignKey("pokemons.id")),
)

    
class TeamDBModel(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    team_pokemons : Mapped[List[PokemonDBModel]] = relationship(secondary="team_pokemon_association_table")
    __table_args__ = (UniqueConstraint("name"),)
    