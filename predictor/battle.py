# Attack Simluator
#     Implemented:
#         basic formula for dealing damage
#         HP bars go down after Attacks
#         simple text display
#         testing for tackle
#     Pending
#         When is something supereffective????
#         crits?
#         rand factor?
#         testing of more attacks... more pokemon....

import random

# def createTypeDict():
#     type_dict = {}
#     type_dict['normal'] = 0
#     type_dict['fire'] = 1
#     type_dict['water'] = 2
#     type_dict['electric'] = 3
#     type_dict['grass'] = 4
#     type_dict['ice'] = 5
#     type_dict['fighting'] = 6
#     type_dict['poison'] = 7
#     type_dict['ground'] = 8
#     type_dict['flying'] = 9
#     type_dict['psychic'] = 10
#     type_dict['bug'] = 11
#     type_dict['rock'] = 12
#     type_dict['ghost'] = 13
#     type_dict['dragon'] = 14
#     type_dict['dark'] = 15
#     type_dict['steel'] = 16
#     type_dict['fairy'] = 17
#     return type_dict
#
#
# def instantiateMatrix():
#     """
#     look up effectiveness in a large matrix
#            each value in the matrix is stored as 0, 0.5, 1, or 2
#            see http://pokemondb.net/type
#     """
#     type_dict = createTypeDict()
#     type_matrix = [[1 for _ in range(18)] for _ in range(18)]
#     type_matrix[type_dict['normal']][type_dict['fighting']] = 2
#     type_matrix[type_dict['normal']][type_dict['ghost']] = 0
#     type_matrix[type_dict['fire']][type_dict['fire']] = 0.5
#     type_matrix[type_dict['fire']][type_dict['water']] = 2
#     type_matrix[type_dict['fire']][type_dict['grass']] = 0.5
#     type_matrix[type_dict['fire']][type_dict['ice']] = 0.5
#     type_matrix[type_dict['fire']][type_dict['ground']] = 2
#     type_matrix[type_dict['fire']][type_dict['bug']] = 0.5
#     type_matrix[type_dict['fire']][type_dict['rock']] = 2
#     type_matrix[type_dict['fire']][type_dict['steel']] = 0.5
#     type_matrix[type_dict['fire']][type_dict['fairy']] = 0.5
#     type_matrix[type_dict['water']][type_dict['fire']] = 0.5
#     type_matrix[type_dict['water']][type_dict['fire']] = 0.5
#     type_matrix[type_dict['water']][type_dict['water']] = 0.5
#     type_matrix[type_dict['water']][type_dict['grass']] = 2
#     type_matrix[type_dict['water']][type_dict['ice']] = 0.5
#     type_matrix[type_dict['water']][type_dict['steel']] = 0.5
#     type_matrix[type_dict['electric']][type_dict['electric']] = 0.5
#     type_matrix[type_dict['electric']][type_dict['ground']] = 2
#     type_matrix[type_dict['electric']][type_dict['electric']] = 0.5



class Attack:
    def __init__(self, att_poke, def_poke, move):
        """the att_poke attacks def_poke, using move"""
        self.att_poke = att_poke
        self.def_poke = def_poke
        self.move = move

    def __str__(self):
        return self.att_poke.name + " used " + self.move.name + " on " + self.def_poke.name + "!"

    def find_effectiveness(self):
        """The type matrix is [defender][attacker]
           """
        return 1

    def find_crit(self):
        """Crits double the damage - calculate this...""" # FIX
        return 1

    def find_stab(self):
        """Pokemon deals 1.5 times normal damage if same type as the move
           Return True if applicable"""
        if self.move.type == self.att_poke.pType or self.move.type == self.att_poke.sType:
            return 1.5
        return 1

    def find_other(self):
        """factor for other effects such as items, abilities, field advantages... etc""" # FIX
        return 1

    def find_rand(self):
        """Attacks deal anywhere between 85% (inclusive) and 100% (exclusive) of their theoretical damage""" #Fix
        # return random.uniform(0.85, 1)
        return 1

    def find_damage(self):
        """Calculate the damage and subtract that amount from defender
           http://bulbapedia.bulbagarden.net/wiki/Damage#Damage_formula"""
        if self.move.cat == 'Physical':
            attack = self.att_poke.att
            defense = self.def_poke.dfn
        elif self.move.cat == 'Special':
            attack = self.att_poke.spA
            defense = self.def_poke.spD
        else: # status moves deal no damage
            attack = 0
            defense = 9001
        base_damage = (((2.0*self.att_poke.lvl + 10) / 250) * attack / defense * self.move.pow) + 2
        modifier = (self.find_stab() * self.find_effectiveness() * self.find_crit() * self.find_other() * self.find_rand())
        damage = int(base_damage*modifier)
        self.def_poke.cHP -= damage
        return damage

    def check_fainted(self):
        if self.def_poke.cHP <= 0:
            return "...RIP The defending " + self.def_poke.name + " fainted"
        else:
            return "...The defending " + self.def_poke.name + " has " + str(self.def_poke.cHP) + " HP remaining"






