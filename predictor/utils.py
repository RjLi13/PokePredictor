__author__ = 'ruijing and josh'


import pykemon
from pokemon import *
from battle import *
import json

DEFAULT = '<blank>'

json_data = open('predictor/bw.json')
set_bw = json.load(json_data)

json_data = open('predictor/dpp.json')
set_dpp = json.load(json_data)

json_data = open('predictor/gse.json')
set_rse = json.load(json_data)

json_data = open('predictor/gsc.json')
set_gsc = json.load(json_data)

json_data = open('predictor/rby.json')
set_rby = json.load(json_data)


def choose_move(name, lvl, cHP, nature, ability, opp_name, opp_lvl, opp_cHP, opp_nature, opp_ability, move1, move2, move3, move4):
    pokemon = get_Pokemon(name, lvl, cHP, nature, ability)
    opp_pokemon = get_Pokemon(opp_name, opp_lvl, opp_cHP, opp_nature, opp_ability)
    move1 = find_move_info(name, move1)
    move2 = find_move_info(name, move2)
    move3 = find_move_info(name, move3)
    move4 = find_move_info(name, move4)
    moves = [move1, move2, move3, move4]
    tackle = Move('Tackle', 'Normal', 'Physical', 50, 100, DEFAULT)
    tail_whip = Move('Tail Whip', 'Normal', 'Status', 50, 30, 'Lowers Opponent\'s Defense')
    water_gun = Move('Water Gun', 'Water', 'Special', 40, 100, DEFAULT)
    thunder_shock = Move('Thunder Shock', 'Electric', 'Special', 40, 100, 'May paralyze opponent')
    moves = [tackle, tail_whip, water_gun, thunder_shock]
    dmg = 0
    move_chosen = None
    for move in moves:
        new_dmg = Attack(pokemon, opp_pokemon, move).find_damage()
        if new_dmg > dmg or (new_dmg == dmg and move.acc > move_chosen.acc):
            move_chosen = move
            dmg = new_dmg
    return move_chosen

def find_move_info(poke_name, move_name):
    try:
        poke_data = pykemon.get(pokemon=poke_name.lower())
    except KeyError:
        DEFAULT_POKEMON = Pokemon(DEFAULT, 0, 0, 0, 0, 0, 0, 0, 0, DEFAULT, DEFAULT)
        return DEFAULT_POKEMON
    moves = poke_data.moves
    if move_name in moves:
        get_info = moves[move_name]
        get_info = str(get_info)
        strlen = len(get_info)
        move_id = get_info[11:strlen-1]
        move_id = int(move_id)
        move_data = pykemon.get(move_id=move_id)
        #TODO figure out type and category on pokeapi!!!
        return Move(move_data.name, DEFAULT, move_data.category, move_data.power, move_data.accuracy, move_data.description, move_data.pp)

    else:
        DEFAULT_MOVE = Move(DEFAULT, DEFAULT, DEFAULT, 0, 100, DEFAULT)
        return DEFAULT_MOVE



def get_Pokemon(name, lvl, cHP, nature, ability):
    try:
        poke_data = pykemon.get(pokemon=name.lower())
    except KeyError:
        DEFAULT_POKEMON = Pokemon(DEFAULT, 0, 0, 0, 0, 0, 0, 0, 0, DEFAULT, DEFAULT)
        return DEFAULT_POKEMON

    if not check_validity(lvl, cHP, nature, ability):
        DEFAULT_POKEMON = Pokemon(DEFAULT, 0, 0, 0, 0, 0, 0, 0, 0, DEFAULT, DEFAULT)
        return DEFAULT_POKEMON
    poke_name = poke_data.name
    poke_atk = poke_data.attack
    poke_def = poke_data.defense
    poke_spatk = poke_data.sp_atk
    poke_spdef = poke_data.sp_def
    poke_speed = poke_data.speed
    poke_types = poke_data.types
    poke_pType = poke_types.keys()[0]
    poke_sType = poke_pType
    poke_lvl = lvl
    poke_mHp = poke_data.hp
    poke_cHp = cHP / 100 * poke_mHp
    poke_nature = nature
    poke_ability = ability
    if len(poke_types) == 2:
        poke_pType = poke_types.keys()[1]
    pokemon = Pokemon(poke_name, poke_lvl, poke_mHp, poke_cHp, poke_atk, poke_def, poke_spatk, poke_spdef, poke_speed, poke_pType, poke_sType, poke_nature, poke_ability)
    return pokemon

def check_validity(lvl, cHP, nature, ability):
    if lvl < 0 or lvl > 100:
        return False
    if cHP < 0 or cHP > 100:
        return False
    return True

