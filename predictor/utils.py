__author__ = 'ruijing and josh'


import pykemon
from pokemon import *
from battle import *
import json
import urllib2
import random

DEFAULT = '<blank>'

json_data = open('predictor/bw.json')
set_bw = json.load(json_data)

# json_data = open('predictor/dpp.json')
# set_dpp = json.load(json_data)
#
# json_data = open('predictor/gse.json')
# set_rse = json.load(json_data)
#
# json_data = open('predictor/gsc.json')
# set_gsc = json.load(json_data)
#
# json_data = open('predictor/rby.json')
# set_rby = json.load(json_data)


def makeCapitalString(word):
    word = str(word)
    word = word.lower()
    upper_char = word[0].upper()
    word = upper_char + word[1:]
    return word

def choose_move(name, lvl, cHP, nature, ability, opp_name, opp_cHP,
                move1, move2, move3, move4,  move1_type, move2_type, move3_type, move4_type, move1_category,
                move2_category, move3_category, move4_category, item, num_pokemon, opp_num_pokemon, evs):
    if not item:
        item = DEFAULT
    if not ability:
        ability = DEFAULT
    pokemon = get_Pokemon(name, lvl, cHP, nature, ability, item, evs)
    opp_name = makeCapitalString(opp_name)
    opp_pokemon = get_opponent_info(opp_name, opp_cHP)

    move1 = find_move_info(name, move1, move1_type, move1_category)
    move2 = find_move_info(name, move2, move2_type, move2_category)
    move3 = find_move_info(name, move3, move3_type, move3_category)
    move4 = find_move_info(name, move4, move4_type, move4_category)
    moves = [move1, move2, move3, move4]
    dmg = 0
    move_chosen = None
    for move in moves:
        # print move
        new_dmg = Attack(pokemon, opp_pokemon, move).find_damage()
        if new_dmg > dmg or (new_dmg == dmg and move.acc > move_chosen.acc):
            move_chosen = move
            dmg = new_dmg
    return move_chosen

def get_opponent_info(opp_name, opp_cHP):
    poke_sets = set_bw[opp_name]
    try:
        poke_data = pykemon.get(pokemon=opp_name.lower())
    except KeyError:
        DEFAULT_POKEMON = Pokemon(DEFAULT, 0, 0, 0, 0, 0, 0, 0, 0, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, {})
        return DEFAULT_POKEMON

    # TODO how to determine which set to use?
    poke_sets_keys = list(poke_sets.keys())
    index = random.randint(0, len(poke_sets_keys)-1)
    poke_set_key = poke_sets_keys[index]
    poke_set = poke_sets[poke_set_key]
    poke_types = poke_data.types
    poke_pType = poke_types.keys()[0]
    poke_sType = poke_pType
    if len(poke_types) == 2:
        poke_pType = poke_types.keys()[1]
    opp_cHP = opp_cHP/100 * poke_data.hp
    pokemon = Pokemon(opp_name, poke_set['level'], poke_data.hp, opp_cHP, poke_data.attack,
                      poke_data.defense, poke_data.sp_atk, poke_data.sp_def, poke_data.speed, poke_pType,
                      poke_sType, poke_set['nature'], poke_set['ability'], poke_set['item'], poke_set['evs'])
    #print "Opponent Pokemon %s" %pokemon
    return pokemon


def find_move_info(poke_name, move_name, move_type, move_category):
    makeCapitalString(move_name)
    try:
        poke_data = pykemon.get(pokemon=poke_name.lower())
    except KeyError:
        DEFAULT_MOVE = Move(DEFAULT, DEFAULT, DEFAULT, 0, 100, DEFAULT, DEFAULT)
        return DEFAULT_MOVE
    moves = poke_data.moves
    if move_name in moves:
        get_info = moves[move_name]
        get_info = str(get_info)
        strlen = len(get_info)
        move_id = get_info[13:strlen-1]
        move_id = int(move_id)
        move_data = pykemon.get(move_id=move_id)
        data = json.load(urllib2.urlopen('http://pokeapi.co/api/v1/move/' + str(move_id)))
        description = data['description']
        return Move(move_data.name, move_type, move_category, move_data.power, move_data.accuracy,
                    description, move_data.pp)
    else:
        DEFAULT_MOVE = Move(DEFAULT, DEFAULT, DEFAULT, 0, 100, DEFAULT, DEFAULT)
        return DEFAULT_MOVE



def get_Pokemon(name, lvl, cHP, nature, ability, item, evs):
    try:
        poke_data = pykemon.get(pokemon=name.lower())
    except KeyError:
        DEFAULT_POKEMON = Pokemon(DEFAULT, 0, 0, 0, 0, 0, 0, 0, 0, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, {})
        return DEFAULT_POKEMON

    if not check_validity(lvl, cHP, ability, evs):
        DEFAULT_POKEMON = Pokemon(DEFAULT, 0, 0, 0, 0, 0, 0, 0, 0, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, {})
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
    if len(poke_types) == 2:
        poke_pType = poke_types.keys()[1]
    poke_lvl = lvl
    poke_mHp = poke_data.hp
    poke_cHp = cHP / 100 * poke_mHp
    if not nature:
        nature = DEFAULT
    if not ability:
        ability = DEFAULT
    if not item:
        item = DEFAULT
    poke_nature = nature
    poke_ability = ability
    pokemon = Pokemon(poke_name, poke_lvl, poke_mHp, poke_cHp, poke_atk,
                      poke_def, poke_spatk, poke_spdef, poke_speed, poke_pType,
                      poke_sType, poke_nature, poke_ability, item, evs)
    #print "My Pokemon %s" %pokemon
    return pokemon

def check_validity(lvl, cHP, ability, evs):
    if lvl < 0 or lvl > 100:
        return False
    if cHP < 0 or cHP > 100:
        return False
    for key, value in evs.items():
        if value > 252 or value < 0:
            return False
    return True

