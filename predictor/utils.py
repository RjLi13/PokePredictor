# all game strategy (choosing moves, choosing whether or not to switch)


__author__ = 'ruijing and josh'


import pykemon # RJ - I commented this out to compile with python3
from pokemon import *
from battle import *
import json # RJ - I commented this out to compile with python3
import urllib2 # RJ - I commented this out to compile with python3
import random
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT = '<blank>'

json_data = open(os.path.join(BASE_DIR, 'predictor/bw.json')) # RJ - I commented this out to compile with python3
set_bw = json.load(json_data) # RJ - I commented this out to compile with python3

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
    """
    Makes word Capital
    :param word:
    :return: word
    """
    word = str(word)
    word = word.lower()
    upper_char = word[0].upper()
    word = upper_char + word[1:]
    return word

def choose_move(name, lvl, cHP, nature, ability, opp_name, opp_cHP,
                move1, move2, move3, move4,  move1_type, move2_type, move3_type, move4_type, move1_category,
                move2_category, move3_category, move4_category, item, num_pokemon, opp_num_pokemon, evs):
    """
    Predicts the move
    :param name:
    :param lvl:
    :param cHP:
    :param nature:
    :param ability:
    :param opp_name:
    :param opp_cHP:
    :param move1:
    :param move2:
    :param move3:
    :param move4:
    :param move1_type:
    :param move2_type:
    :param move3_type:
    :param move4_type:
    :param move1_category:
    :param move2_category:
    :param move3_category:
    :param move4_category:
    :param item:
    :param num_pokemon:
    :param opp_num_pokemon:
    :param evs:
    :return: Returns best move
    """
    if not item:
        item = DEFAULT
    if not ability:
        ability = DEFAULT
    pokemon = get_Pokemon(name, lvl, cHP, nature, ability, item, evs)
    opp_name = makeCapitalString(opp_name)
    opp_pokemon_info = get_opponent_info(opp_name, opp_cHP)
    opp_pokemon = opp_pokemon_info[0]
    opp_pokemon_moveset = opp_pokemon_info[1]
    opp_moves = []
    for move in opp_pokemon_moveset:
        opp_moves.append(find_move_info(opp_pokemon.name, move, opp_pokemon.pType))
        opp_moves.append(find_move_info(opp_pokemon.name, move, opp_pokemon.sType))
    move1 = find_move_info(name, move1, move1_type, move1_category)
    move2 = find_move_info(name, move2, move2_type, move2_category)
    move3 = find_move_info(name, move3, move3_type, move3_category)
    move4 = find_move_info(name, move4, move4_type, move4_category)
    moves = [move1, move2, move3, move4]
    moves = reverse_sort_moves(pokemon, opp_pokemon, moves)
    """ The logic here is that first we get the status moves which will be in the rest of the list because all pokemon
    sets logically speaking should have a move that deals damage in case of being taunted. Then we choose the highest
    power move as move_chosen. However, usually, the highest power move has bad accuracy so we would want to choose
    a less powerful move but can guareentee a hit. 85% chance of hitting is a good accuracy but it can't be a bad move
    that deals almost no damage at all. That's why since the list is ranked from highest damage to lowest, the second
    move is often in the list is often good enough to use. Status moves are often used in the beginning when you are
    in a good position early in the game and you can't deal enough damage, and you aren't locked by choice item. Switch
     is calculated first to check if we will be killed or not.
    """
    status_moves = []
    for move in moves:
        if move.cat == 'Status':
            status_moves.append(move)
    move_chosen = moves[0]
    dmg = Attack(pokemon, opp_pokemon, move_chosen).find_damage()
    dmg_done = float(opp_pokemon.cHP)/opp_pokemon.mHP * 100 - float(opp_pokemon.cHP-dmg)/opp_pokemon.mHP * 100
    alt_move = moves[1]
    new_dmg = Attack(pokemon, opp_pokemon, alt_move).find_damage()
    if alt_move.acc > move_chosen.acc and alt_move.acc >= 80:
        temp_dmg_done = float(opp_pokemon.cHP)/opp_pokemon.mHP * 100 - \
                       float(opp_pokemon.cHP-new_dmg)/opp_pokemon.mHP * 100
        if temp_dmg_done > 60 or opp_cHP < 30:
            move_chosen = alt_move
            dmg = new_dmg
            dmg_done = temp_dmg_done
    if not num_pokemon:
        num_pokemon = 6
    if should_switch(opp_pokemon, pokemon, opp_moves, num_pokemon, dmg):
        return ("Switch", 0)
    if cHP > 85 and dmg_done < 60 and opp_cHP > 50 and len(status_moves) > 0:
        if len(item) <= 7 or len(item) > 7 and item[0:6] != 'choice':
            index = random.randint(0, len(status_moves)-1)
            return (status_moves[index].name, 0)
    return (move_chosen.name, dmg_done)

#Highest power move will always be in front, the first element of list after sorted
def reverse_sort_moves(pokemon, opp_pokemon, moves):
    unsorted = []
    dict = {}
    sorted = [None, None, None, None]
    for move in moves:
        dmg = Attack(pokemon, opp_pokemon, move).find_damage()
        if move in dict:
            old_dmg = dict[move]
            if old_dmg < dmg:
                dict[move] = dmg
                unsorted.remove(old_dmg)
                unsorted.append(dmg)
        else:
            dict[move] = dmg
            unsorted.append(dmg)

    unsorted = my_sort(unsorted)
    # print len(unsorted)
    for key, value in dict.items():
        for index in range(0, len(unsorted)):
            if value == unsorted[index]:
                sorted[index] = key
    return sorted


def my_sort(array):
    if len(array) > 5:
        random.shuffle(array)
        quick_sort(array, 0, len(array) - 1)
    else:
        array = insert_sort(array)
    return array


def insert_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] > array[j-1]:
                swap(array, j, j-1)
    return array


def quick_sort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quick_sort(array, low, pivot)
        quick_sort(array, pivot+1, high)


def partition(array, low, high):
    pivot = array[low]
    i = low -1
    j = high + 1
    while 1:
        j -= 1
        while array[j] < pivot:
            j -= 1
        i += 1
        while array[i] > pivot:
            i += 1
        if i < j:
            swap(array, i, j)
        else:
            return j

def swap(array, i, j):
    temp = array[j]
    array[j] = array[i]
    array[i] = temp

def get_opponent_info(opp_name, opp_cHP):
    """
    Gets opponent's pokemon and moveset
    :param opp_name:
    :param opp_cHP:
    :return: tuple containing pokemon and moveset
    """
    poke_sets = set_bw[opp_name]
    try:
        # poke_data = json.load(urllib2.urlopen("http://pokeapi.co/api/v1/pokemon/" + opp_name.lower()))
        poke_data = pykemon.get(pokemon=opp_name.lower())
    except KeyError:
        DEFAULT_POKEMON = Pokemon(DEFAULT, 0, 0, 0, 0, 0, 0, 0, 0, DEFAULT, DEFAULT, DEFAULT, DEFAULT, DEFAULT, {})
        return DEFAULT_POKEMON

    # TODO how to determine which set to use?
    poke_sets_keys = list(poke_sets.keys())
    index = random.randint(0, len(poke_sets_keys)-1)
    poke_set_key = poke_sets_keys[index]
    poke_set = poke_sets[poke_set_key]
    # poke_types = poke_data['types']
    poke_types = poke_data.types
    poke_pType = poke_types.keys()[0]
    # poke_pType = poke_types[0]['name']
    poke_sType = poke_pType
    if len(poke_types) == 2:
        poke_pType = poke_types.keys()[1]
        # poke_pType = poke_types[1]['name']
    pokemon = Pokemon(opp_name, poke_set['level'], poke_data.hp, opp_cHP, poke_data.attack,
                      poke_data.defense, poke_data.sp_atk, poke_data.sp_def, poke_data.speed, poke_pType,
                      poke_sType, poke_set['nature'], DEFAULT, poke_set['item'], poke_set['evs'])
    # pokemon = Pokemon(opp_name, poke_set['level'], poke_data['hp'], opp_cHP, poke_data['attack'],
    #                   poke_data['defense'], poke_data['sp_atk'], poke_data['sp_def'], poke_data['speed'], poke_pType,
    #                   poke_sType, poke_set['nature'], DEFAULT, poke_set['item'], poke_set['evs'])
    opp_moveset = poke_set['moves']
    # print "Opponent Pokemon %s" %pokemon
    # print opp_moveset
    return (pokemon, opp_moveset)


def find_move_info(poke_name, move_name, move_type='Normal', move_category='Physical'):
    """
    Gets your moves
    :param poke_name:
    :param move_name:
    :param move_type:
    :param move_category:
    :return: move object
    """
    makeCapitalString(move_name)
    try:
        # poke_data = json.load(urllib2.urlopen("http://pokeapi.co/api/v1/pokemon/" + poke_name.lower()))
        # print poke_data
        poke_data = pykemon.get(pokemon=poke_name.lower())
    except KeyError:
        DEFAULT_MOVE = Move(DEFAULT, DEFAULT, DEFAULT, 0, 100, DEFAULT, DEFAULT)
        return DEFAULT_MOVE
    moves = poke_data.moves
    # moves = poke_data['moves']
    # for move in moves:
    #     if move_name in move.values():
    if move_name in moves:
        get_info = moves[move_name]
        # get_info = move['resource_uri']
        get_info = str(get_info)
        str_len = len(get_info)
        move_id = get_info[13:str_len-1]
        move_id = int(move_id)
        # print move_id
        # move_data = pykemon.get(move_id=move_id)
        data = json.load(urllib2.urlopen('http://pokeapi.co/api/v1/move/' + str(move_id)))
        description = data['description']
        # return Move(move_data.name, move_type, move_category, move_data.power, move_data.accuracy,
        #             description, move_data.pp)
        return Move(data['name'], move_type, move_category, data['power'], data['accuracy'],
                    description, data['pp'])
    else:
        DEFAULT_MOVE = Move(DEFAULT, DEFAULT, DEFAULT, 0, 100, DEFAULT, DEFAULT)
        return DEFAULT_MOVE



def get_Pokemon(name, lvl, cHP, nature, ability, item, evs):
    """
    Gets pokemon info
    :param name:
    :param lvl:
    :param cHP:
    :param nature:
    :param ability:
    :param item:
    :param evs:
    :return: Pokemon object
    """
    try:
        # poke_data = json.load(urllib2.urlopen("http://pokeapi.co/api/v1/pokemon/" + name.lower()))
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
    poke_mHP = poke_data.hp
    # poke_name = poke_data['name']
    # poke_atk = poke_data['attack']
    # poke_def = poke_data['defense']
    # poke_spatk = poke_data['sp_atk']
    # poke_spdef = poke_data['sp_def']
    # poke_speed = poke_data['speed']
    # poke_types = poke_data['types']
    # poke_mHP = poke_data['hp']
    # poke_pType = poke_types[0]['name']
    poke_pType = poke_types.keys()[0]
    poke_sType = poke_pType
    if len(poke_types) == 2:
        poke_pType = poke_types.keys()[1]
        # poke_pType = poke_types[1]['name']
    poke_lvl = lvl

    poke_cHP = cHP
    if not nature:
        nature = DEFAULT
    if not ability:
        ability = DEFAULT
    if not item:
        item = DEFAULT
    poke_nature = nature
    poke_ability = ability
    pokemon = Pokemon(poke_name, poke_lvl, poke_mHP, poke_cHP, poke_atk,
                      poke_def, poke_spatk, poke_spdef, poke_speed, poke_pType,
                      poke_sType, poke_nature, poke_ability, item, evs)
    # print "My Pokemon %s" %pokemon
    return pokemon

def check_validity(lvl, cHP, ability, evs):

    """
    Checks info is valid
    :param lvl:
    :param cHP:
    :param ability:
    :param evs:
    :return: True/False
    """
    if lvl < 0 or lvl > 100:
        return False
    if cHP < 0 or cHP > 100:
        return False
    ev_sum = 0
    for key, value in evs.items():
        if value > 252 or value < 0:
            return False
        ev_sum += value
    if ev_sum > 510:
        return False
    return True


############ Logic for switching ############


# magic number - determining when we should switch
SWITCH_THRESH = 0.2


def should_switch(att_poke, def_poke, att_moves, num_pokemon, def_dmg):
    """ Returns T/F depending of favorability of current matchup
        based on types of attacker and defender

        example - Charmander should switch out if against a Squirtle (rating of -0.25) 
                - Charmander should not switch out against a Caterpie (rating of 0.375)
    """
    if eval_matchup(att_poke, def_poke, att_moves, def_dmg) > SWITCH_THRESH and num_pokemon > 1:
        return True
    return False

    # Alternate logic - requires more processing - consider for later version
    # if bad_matchup:
    #     if pokemon speed faster:
    #         if dmg > dmg opponent does and calculate_survial() for one turn
    #             return false
    #         return true0
    #     else
    #         calculate survival() 
    #         if you deal dmg > dmg they do and survive turns > opp survival
    #             return false
    #         return true
    
    # if bad_matchup(att_poke, def_poke):
    #     if att_poke.spe > def_poke.spe: # we are faster than enemy





def eval_matchup(att_poke, def_poke, att_moves, def_dmg):
    """Return value depending on how good attacker is against the defender
        Notes:
            1 - great for attacker (we have a double super effective move, they can't hurt us)
            0 - neutral
            -1 - terrible for attacker (i.e attacker can't deal any damage) (bad)
                Almost all evaluations will be somewhat close to 0
            
            Will give more precise evaluations in future versions 

        Formula (Ruijing and Josh's unofficial estimation of a matchup) (should improve in later version):
            (Effectiveness of attacker's best move - Effectiveness of defender's type against attacker's type) / 4

            Example calculations:
                
                Charmander (Fire) vs Caterpie (Bug)
                 * Charmander's Ember is super effective against Bug (given a 2)
                 * Bug is 1/2 effective vs Fire 
                 * Total Rating: (2 - 1/2) / 4 = 1.5 / 4 = 0.375 (very good)               

                Charmander (Fire) vs Paras (Bug / Grass)
                 * Charmander's Ember is super effective against both Bug and Grass (given a 4)
                 * Bug is 1/2 effective vs Fire AND Grass is 1/2 effective vs Fire - we average them to get a 1/2
                 * Total Rating: (4 - 1/2) / 4 = 3.5 / 4 = 0.875 (extremely good)

                Charmander (Fire) vs Squirtle (Water)
                 * Charmander's Tackle is Normally effective against Water (given a 1)
                 * Water is x2 effective vs Fire
                 * Total Rating: (1 - 2) / 4 = -1 / 4 = -0.25 (bad)
                     --- even though Charmander optimally uses Tackle, a normal type move, still a bad matchup
        """
        
        # alternative idea - base it on the optimal move... worth considering for a later version
            # optimal_move = choose_move(att_poke.name, att_poke.lvl, att_poke.cHP, att_poke.nature, att_poke.ability, def_poke.name, def_poke.cHP,
            #         att_poke.moves[0], att_poke.moves[1], att_poke.moves[2], att_poke.moves[3], move1_type, move2_type, move3_type, move4_type, move1_category,
            #         move2_category, move3_category, move4_category, item, num_pokemon, opp_num_pokemon, evs)
            # I'm not sure how to get the optimal move from this frame - we don't have enough information
            # optimal_move = att_poke.moves[0] # temp - take the first move
            # first check - do we have a super effective *damage* move against the defending pokemon?

    attack_rating = 0

    # PUT THIS BACK ONCE WE CAN GET THE POKEMON'S MOVESSSS
    moves = reverse_sort_moves(att_poke, def_poke, att_moves)
    move_chosen = moves[0]
    dmg = Attack(att_poke, def_poke, move_chosen).find_damage()
    attack_rating = dmg
    defense_rating = def_dmg
    def_dmg_done = float(att_poke.cHP)/att_poke.mHP * 100 - float(att_poke.cHP-defense_rating)/att_poke.mHP * 100
    if def_poke.spe > att_poke.spe and def_dmg_done > 100:
        return -1
    else:
        return (attack_rating - defense_rating) / 4.0

    # for move in att_moves:
    #     if move.cat != "Status":
    #         sample_attack = Attack(att_poke, def_poke, move)
    #         effectiveness = sample_attack.find_damage()
    #         if effectiveness > attack_rating:
    #             attack_rating = effectiveness
    # temporary fix
    # attack_rating_p = Attack(att_poke, def_poke, Move('test', att_poke.pType))
    # attack_rating_s = Attack(att_poke, def_poke, Move('test', att_poke.sType))
    # attack_rating = (attack_rating_p.find_effectiveness() + attack_rating_s.find_effectiveness()) / 2.0
    #
    # # ideal 'defense ratings' are low - meaning the enemy does not do much damage
    # defense_strat = Attack(def_poke, att_poke, def_move)
    # defense_rating = defense_strat.find_damage()





# defaults
# DEFAULT = '<blank>'
# DEFAULT_MOVE = Move(DEFAULT, DEFAULT, DEFAULT, 0, 100, DEFAULT)
# DEFAULT_POKEMON = Pokemon(DEFAULT, 0, 0, 0, 0, 0, 0, 0, 0, DEFAULT, DEFAULT)
#
# # moves
# tackle = Move('Tackle', 'Normal', 'Physical', 50, 100, DEFAULT)
# tail_whip = Move('Tail Whip', 'Normal', 'Status', 0, 30, 'Lowers Opponent\'s Defense')
# water_gun = Move('Water Gun', 'Water', 'Special', 40, 100, DEFAULT)
# thunder_shock = Move('Thunder Shock', 'electric', 'Special', 40, 100, 'May paralyze opponent')
# thunder_shock = Move('Thunder Shock', 'electric', 'Special', 40, 100, 'May paralyze opponent')
#
# # pokemon
# pikachu = Pokemon('Pikachu', 10, 35, 35, 55, 40, 50, 50, 90, 'electric', 'electric')
# squirtle = Pokemon('Squirtle', 10, 44, 44, 48, 65, 50, 64, 43, 'water', 'water')


# for testing
def report_switch(att_poke, def_poke):
    print("======")
    print(">>> " + att_poke.name + " has a rating of " + str(eval_matchup(att_poke, def_poke)) + " vs enemy " + def_poke.name)
    if should_switch(att_poke, def_poke):
        print(">>> SWITCH")   
    else:
        print(">>> Do not switch")

# report_switch(squirtle, squirtle)
# report_switch(pikachu, squirtle)
# report_switch(squirtle, pikachu)
# report_switch(pikachu, pikachu)
