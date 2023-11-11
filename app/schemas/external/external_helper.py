import json
from typing import List
from app.schemas.external.external_pokemon_schema import ExternalPokemon
from app.schemas.pokemon.ability_schema import PokemonAbility
from app.schemas.pokemon.move_schema import Move, VersionGroupDetails

from app.schemas.pokemon.pokemon_schema import Pokemon
from app.schemas.pokemon.stat_schema import PokemonStat
from app.schemas.pokemon.type_schema import PokemonType
from app.schemas.external import external_ability_schema, external_type_schema, external_move_schema, external_stat_schema

def parse_json_into_external_pokemon(loaded_json: json) -> ExternalPokemon:
    return ExternalPokemon(**loaded_json)

def parse_external_into_internal_types(external_types: List[external_type_schema.PokemonType]) -> List[PokemonType]:
    parsed_types = list()
    for type in external_types:
        parsed_types.append(PokemonType(slot=type.slot,type=type.type.name))
    return parsed_types

def parse_external_into_internal_moves(external_moves: List[external_move_schema.Move]) -> List[Move]:
    parsed_moves = list()
    for move in external_moves:
        parsed_version_group_details = list()
        for version_group in move.version_group_details:
            parsed_version_group_details.append(VersionGroupDetails(move_learn_method=version_group.move_learn_method.name,
                                                                    level_learned_at=version_group.level_learned_at,
                                                                    version_group=version_group.version_group.name))
        parsed_moves.append(Move(move=move.move.name, version_group_details=parsed_version_group_details))
    return parsed_moves

def parse_external_into_internal_stats(external_stats: List[external_stat_schema.PokemonStat]) -> List[PokemonStat]:
    parsed_stats = list()
    for stat in external_stats:
        parsed_stats.append(PokemonStat(stat=stat.stat.name, base_stat=stat.base_stat, effort=stat.effort))
    return parsed_stats

def parse_external_into_internal_abilities(external_abilities: List[external_ability_schema.Ability]) -> List[PokemonAbility]:
    parsed_abilities = list()
    for ability in external_abilities:
        parsed_abilities.append(PokemonAbility(ability=ability.ability.name, is_hidden=ability.is_hidden, slot=ability.slot))
    return parsed_abilities
    

def parse_external_into_internal_pokemon(external_pokemon: ExternalPokemon) -> Pokemon:
    parsed_types = parse_external_into_internal_types(external_pokemon.types)
    parsed_moves = parse_external_into_internal_moves(external_pokemon.moves)
    parsed_stats = parse_external_into_internal_stats(external_pokemon.stats)
    parsed_abilities = parse_external_into_internal_abilities(external_pokemon.abilities)
        
    pokemon = Pokemon(id=external_pokemon.id, name=external_pokemon.name,
                   sprites=external_pokemon.sprites, types=parsed_types, height=external_pokemon.height,
                   weight=external_pokemon.weight, moves=parsed_moves, order=external_pokemon.order, 
                   species=external_pokemon.species.name, stats=parsed_stats, abilities=parsed_abilities,
                   form=external_pokemon.forms[0].name)
    return pokemon


# TODO: Remove
def init_db():
    with open('pokemons.json') as file:
        loaded_json = json.load(file)
        pokemon = parse_external_into_internal_pokemon(parse_json_into_external_pokemon(loaded_json[0]))
        print(pokemon)
                                                                        
