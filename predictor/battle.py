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

class Attack:
    def __init__(self, att_poke, def_poke, move):
        """the att_poke attacks def_poke, using move"""
        self.att_poke = att_poke
        self.def_poke = def_poke
        self.move = move

    def __str__(self):
        return self.att_poke.name + " used " + self.move.name + " on " + self.def_poke.name + "!"

    def find_effectiveness(self):
        """look up effectiveness in a large matrix
           each value in the matrix is stored as 0, 1/2, 1, or 2
           see http://pokemondb.net/type
         """
        typedict = {}
        typedict["normal"] = 0
        typedict["fire"] = 1
        typedict["water"] = 2
        typedict["electric"] = 3
        typedict["grass"] = 4
        typedict["ice"] = 5
        typedict["fighting"] = 6
        typedict["poison"] = 7
        typedict["ground"] = 8
        typedict["flying"] = 9
        typedict["psychic"] = 10
        typedict["bug"] = 11
        typedict["rock"] = 12
        typedict["ghost"] = 13
        typedict["dragon"] = 14
        typedict["dark"] = 15
        typedict["steel"] = 16
        typedict["fairy"] = 17
 
        effective = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, .5, 0, 1, 1, .5, 1],
        [1, .5, .5, 1, 2, 2, 1, 1, 1, 1, 1, 2, .5, 1, .5, 1, 2, 1] ,
        [1, 2, .5, 1, .5, 1, 1, 1, 2, 1, 1, 1, 2, 1, .5, 1, 1, 1] ,
        [1, 1, 2, .5, .5, 1, 1, 1, 0, 2, 1, 1, 1, 1, .5, 1, 1, 1] ,
        [1, .5, 2, 1, .5, 1, 1, .5, 2, .5, 1, .5, 1, 1, .5, 1, .5, 1] ,
        [1, .5, .5, 1, 2, .5, 1, 1, 2, 2, 1, 1, 1, 1, .5, 1, .5, 1] ,
        [2, 1, 1, 1, 1, 2, 1, .5, 1, .5, .5, .5, 2, 0, 1, 2, 2, 5] ,
        [1, 1, 1, 1, 1, 2, 1, .5, 1, .5, .5, .5, 2, 0, 1, 2, 2, 5] ,
        [1, 2, 1, 2, .5, 1, 1, 2, 1, 0, 1, .5, 2, 1, 1, 1, 2, 1] ,
        [1, 1, 1, .5, 2, 1, 2, 1, 1, 1, 1, 2, .5, 1, 1, 1, .5, 1] ,
        [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, .5, 1, 1, 1, 1, 0, .5, 1] ,
        [1, .5, 1, 1, 2, 1, .5, .5, 1, .5, 2, 1, 1, .5, 1, 2, .5, 5] ,
        [1, 2, 1, 1, 1, 2, .5, 1, .5, 2, 1, 2, 1, 1, 1, 1, .5, 1] ,
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, .5, 1, 1] ,
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, .5, 0] ,
        [1, 1, 1, 1, 1, 1, .5, 1, 1, 1, 2, 1, 1, 2, 1, .5, 1, 5] ,
        [1, .5, .5, .5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, .5, 2], 
        [1, .5, 1, 1, 1, 1, 2, .5, 1, 1, 1, 1, 1, 1, 2, 2, .5, 1]] 

        p_effective = effective[typedict[self.move.type.lower()]][typedict[self.def_poke.pType.lower()]]
        if self.def_poke.pType != self.def_poke.sType:
            s_effective = effective[typedict[self.move.type.lower()]][typedict[self.def_poke.sType.lower()]]
            return p_effective*s_effective
        return effective[typedict[self.move.type]][typedict[self.def_poke.pType]]

    def find_crit(self):
        """Crits double the damage - calculate this...
           Will implement crits phase 2 - note it changes based on basic / 1st stage etc """ # FIX
        return 1

    def find_stab(self):
        """Pokemon deals 1.5 times normal damage if same type as the move
           Return True if applicable"""
        if self.move.type == self.att_poke.pType or self.move.type == self.att_poke.sType:
            return 1.5
        return 1

    def find_other(self):
        """factor for other effects such as items, abilities, field advantages... etc
           will implement phase 2 """ # FIX
        item = self.att_poke.item.lower()
        if len(item) > 7 and item[0:6] == 'choice' and item != 'choice scarf':
            return 2
        if item == 'life orb':
            return 1.3
        return 1

    def find_rand(self):
        """Attacks deal anywhere between 85% and 100% of their theoretical damage
           Note: for E[X] calculations - set to average (uniform distribution)"""
        
        return (0.85+1.0)/2

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
            return 0
        base_damage = (((2.0*self.att_poke.lvl + 10) / 250) * attack / defense * self.move.pow) + 2
        modifier = (self.find_stab() * self.find_effectiveness() * self.find_crit() * 
                        self.find_other() * self.find_rand())
        # print(base_damage, modifier)
        damage = int(base_damage*modifier)
        # self.def_poke.cHP -= damage
        return damage

    def report_results(self, damage):
        """inform user how much damage the attack would deal"""
        return "> " + self.att_poke.name + " dealt " + str(damage) + " damage to " + self.def_poke.name + '!'

    def check_fainted(self):
        if self.def_poke.cHP <= 0:
            return "...RIP The defending " + self.def_poke.name + " fainted"
        else:
            return "...The defending " + self.def_poke.name + " has " + str(self.def_poke.cHP) + " HP remaining" 

    def play(self):
        print(self.report_results(self.find_damage()))
        print(self.check_fainted())