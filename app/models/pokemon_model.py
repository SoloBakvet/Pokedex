from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.database import Base

    
class PokemonDBModel(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    sprites = relationship("SimpleSpriteDBModel", uselist=False, back_populates="pokemon")
    types = relationship("PokemonTypeDBModel", back_populates="pokemon")
    __table_args__ = (UniqueConstraint("name"),)
    
    def __int__(self):
        return 25
    
class SimpleSpriteDBModel(Base):
    __tablename__ = "simple_sprites"
    
    id = Column(Integer, primary_key=True, index=True)
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"))
    front_default = Column(String, index=True)

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

    

