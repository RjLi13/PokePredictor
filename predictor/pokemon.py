# Basic Framework for pokemon and their moves

class Pokemon:
    def __init__(self, name, lvl, mHP, cHP, att, dfn, spA, spD, spe, pType, sType, nature, ability):
        """
            name: 'pikachu'
            level: 1 to 100
            mHP: Max Hit Points (ex: 55)
            cHP: Current Hit Points (ex: 40)
            att: Attack (ex: 55)
            dfn: Defense (ex: 40)
            spA: Special Attack (ex: 50)
            spD: Special Defense (ex: 50)
            spe: Speed (ex: 90)
            pType: Primary Type (Electric)
            sType: Secondary Type - same as primary type if no secondary type (Electric)
            Nature: Nature of pokemon, affects stats
            Ability: Ability of pokemon, may affect moves, stats, opponent pokemon, etc
        """
        # assign instance variables for each of the traits
        self.name = name
        self.lvl = lvl
        self.mHP = mHP
        self.cHP = cHP
        self.att = att
        self.dfn = dfn
        self.spA = spA
        self.spD = spD
        self.spe = spe
        self.pType = pType
        self.sType = sType
        self.nature = nature
        self.ability = ability
    
    def __str__(self):
        """get a printout of all pokemon's info"""

        return '================' + '\n' + self.name.upper() + \
            '\n Level: ' + str(self.lvl) + \
            '\n Max HP: ' + str(self.mHP) + \
            '\n Current HP: ' + str(self.cHP) + \
            '\n Attack: ' + str(self.att) + \
            '\n Defense: ' + str(self.dfn) + \
            '\n Special Attack: ' + str(self.spA) + \
            '\n Special Defense: ' + str(self.spD) + \
            '\n Speed: ' + str(self.spe) + \
            '\n Primary Type: ' + self.pType + \
            '\n Secondary Type: ' + self.sType + \
            '\n Nature: ' + self.nature + \
            '\n Ability: ' + self.ability + \
            '\n================'



class Move:
    def __init__(self, 
        name, type, cat, pow, acc, eff):
        """
            name: 'Tackle'
            type: 'Normal'
            cat: Category {Physical, Special, or Status(not damage dealing)} (ex: Physical)
            pow: Power (ex: 50)
            acc: Accuracy up to 100 (ex: 100)
            eff: Optional Effect Text to be implemented later (ex: <blank> b/c no text)
        """
        # assign instance variables for each of the traits
        self.name = name
        self.type = type
        self.cat = cat
        self.pow = pow
        self.acc = acc
        self.eff = eff

    def __str__(self):
        """get a printout of all move's info"""

        return '================' + '\n' + self.name.upper() + \
            '\n Type: ' + self.type + \
            '\n Category: ' + self.cat + \
            '\n Power: ' + str(self.pow) + \
            '\n Accuracy: ' + str(self.acc) + \
            '\n Effect: ' + self.eff + \
            '\n================'

