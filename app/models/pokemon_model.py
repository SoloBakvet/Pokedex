from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.database import Base

    
class PokemonDBModel(Base):
    __tablename__ = "pokemons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
    details = relationship("PokemonDetailsDBModel", uselist=False, back_populates="pokemon")
    types = relationship("PokemonTypeDBModel", back_populates="pokemon")
    sprites = relationship("SimpleSpriteDBModel", uselist=False, back_populates="pokemon")

    __table_args__ = (UniqueConstraint("name"),)
    
class PokemonDetailsDBModel(Base):
    __tablename__ = "pokemon_details"

    id = Column(Integer, primary_key=True, index=True)
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"))
    
    height = Column(Integer, index=True)
    weight = Column(Integer, index=True)
    order = Column(Integer, index=True)
    species = Column(String, index=True)
    
    sprites = relationship("AdvancedSpriteDBModel", uselist=False, back_populates="pokemon_details")
    pokemon = relationship("PokemonDBModel", uselist=False, back_populates="details")

    __table_args__ = (UniqueConstraint("pokemon_id"),)
    
class SimpleSpriteDBModel(Base):
    __tablename__ = "simple_sprites"
    
    id = Column(Integer, primary_key=True, index=True)
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"))
    
    front_default = Column(String, index=True)

    pokemon = relationship("PokemonDBModel", back_populates="sprites")
    __table_args__ = (UniqueConstraint("pokemon_id"),)
    
class AdvancedSpriteDBModel(Base):
    __tablename__ = "advanced_sprites"
    
    id = Column(Integer, primary_key=True, index=True)
    details_id = Column(Integer, ForeignKey("pokemon_details.id"))
    
    front_default = Column(String, index=True)
    front_female = Column(String, index=True, nullable=True)
    front_shiny = Column(String, index=True)
    front_shiny_female = Column(String, index=True, nullable=True)
    back_default = Column(String, index=True)
    back_female = Column(String, index=True, nullable=True)
    back_shiny = Column(String, index=True)
    back_shiny_female = Column(String, index=True, nullable=True)

    pokemon_details = relationship("PokemonDetailsDBModel", back_populates="sprites")
    __table_args__ = (UniqueConstraint("details_id"),)
    
class PokemonTypeDBModel(Base):
    __tablename__ = "pokemon_types"

    id = Column(Integer, primary_key=True, index=True)
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"))
    
    slot = Column(Integer, index=True)
    type = Column(String, index=True)
    
    pokemon = relationship("PokemonDBModel", uselist=False, back_populates="types")
    __table_args__ = (UniqueConstraint("pokemon_id", "slot"),)

    

