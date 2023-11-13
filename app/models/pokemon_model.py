from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.database import Base

    
class PokemonDBModel(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    
    name = Column(String, index=True)
    height = Column(Integer, index=True)
    weight = Column(Integer, index=True)
    order = Column(Integer, index=True)
    species = Column(String, index=True)
    form = Column(String, index=True)
    
    
    types = relationship("PokemonTypeDBModel", back_populates="pokemon")
    sprites = relationship("PokemonSpritesDBModel", uselist=False, back_populates="pokemon")
    stats = relationship("PokemonStatDBModel", back_populates="pokemon")
    abilities = relationship("PokemonAbilityDBModel", back_populates="pokemon")
    moves = relationship("PokemonMoveDBModel", back_populates="pokemon")

    __table_args__ = (UniqueConstraint("name"),)
    
class PokemonSpritesDBModel(Base):
    __tablename__ = "pokemon_sprites"
    
    id = Column(Integer, primary_key=True, index=True)
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"))
    
    front_default = Column(String, index=True)
    front_female = Column(String, index=True, nullable=True)
    front_shiny = Column(String, index=True)
    front_shiny_female = Column(String, index=True, nullable=True)
    back_default = Column(String, index=True)
    back_female = Column(String, index=True, nullable=True)
    back_shiny = Column(String, index=True)
    back_shiny_female = Column(String, index=True, nullable=True)

    pokemon = relationship("PokemonDBModel", back_populates="sprites")
    __table_args__ = (UniqueConstraint("pokemon_id"),)
    
class PokemonTypeDBModel(Base):
    __tablename__ = "pokemon_types"

    id = Column(Integer, primary_key=True, index=True)
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"))
    
    slot = Column(Integer, index=True)
    type = Column(String, index=True)
    
    pokemon = relationship("PokemonDBModel", uselist=False, back_populates="types")
    __table_args__ = (UniqueConstraint("pokemon_id", "slot"),)
    
class PokemonStatDBModel(Base):
    __tablename__ = "pokemon_stats"
    
    id = Column(Integer, primary_key=True, index=True)
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"))
    
    stat = Column(String, index=True)
    base_stat = Column(String, index=True)
    effort = Column(String, index=True)
    
    pokemon = relationship("PokemonDBModel", uselist=False, back_populates="stats")
    
class PokemonAbilityDBModel(Base):
    __tablename__ = "pokemon_abilities"
    
    id = Column(Integer, primary_key=True, index=True)
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"))
    
    ability = Column(String, index=True)
    is_hidden = Column(Boolean, index=True)
    slot = Column(Integer, index=True)
    
    pokemon = relationship("PokemonDBModel", uselist=False, back_populates="abilities")
    __table_args__ = (UniqueConstraint("pokemon_id", "slot"),)
    
class PokemonMoveDBModel(Base):
    __tablename__ = "pokemon_moves"
    
    id = Column(Integer, primary_key=True, index=True)
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"))
    
    move = Column(String, index=True)

    pokemon = relationship("PokemonDBModel", uselist=False, back_populates="moves")
    version_group_details = relationship("VersionGroupDetailsDBModel", back_populates="move")
    
class VersionGroupDetailsDBModel(Base):
    __tablename__ = "version_group_details"
    
    id = Column(Integer, primary_key=True, index=True)
    move_id = Column(Integer, ForeignKey("pokemon_moves.id"))
    
    move_learn_method = Column(String, index=True)
    version_group = Column(String, index=True)
    level_learned_at = Column(Integer, index=True)
    
    move = relationship("PokemonMoveDBModel", uselist=False, back_populates="version_group_details")
    
    

