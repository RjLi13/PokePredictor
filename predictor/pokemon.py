# Basic Framework for pokemon and their moves

NATURES = {
    'Adamant':['at','sa'],
    'Bashful':['',''],
    'Bold':['df','at'],
    'Brave':['at','sp'],
    'Calm':['sd','at'],
    'Careful':['sd','sa'],
    'Docile':['',''],
    'Gentle':['sd','df'],
    'Hardy':['',''],
    'Hasty':['sp','df'],
    'Impish':['df','sa'],
    'Jolly':['sp','sa'],
    'Lax':['df','sd'],
    'Lonely':['at','df'],
    'Mild':['sa','df'],
    'Modest':['sa','at'],
    'Naive':['sp','sd'],
    'Naughty':['at','sd'],
    'Quiet':['sa','sp'],
    'Quirky':['',''],
    'Rash':['sa','sd'],
    'Relaxed':['df','sp'],
    'Sassy':['sd','sp'],
    'Serious':['',''],
    'Timid':['sp','at']
}


class Pokemon:
    def __init__(self, name, lvl, mHP, cHP, att, dfn, spA, spD, spe, pType, sType, nature, ability, item, evs):

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
            Item: Item Pokemon is currently holding
            Evs: Stat boosters
        """
        # assign instance variables for each of the traits
        self.name = name
        self.lvl = lvl
        self.pType = pType
        self.sType = sType
        self.nature = nature
        self.ability = ability
        self.item = item
        iv = 31
        if 'at' not in evs:
            evs['at'] = 0
        if 'df' not in evs:
            evs['df'] = 0
        if 'sa' not in evs:
            evs['sa'] = 0
        if 'sd' not in evs:
            evs['sd'] = 0
        if 'sp' not in evs:
            evs['sp'] = 0
        if 'hp' not in evs:
            evs['hp'] = 0
        self.evs = evs
        self.att = ((att * 2 + iv + evs['at']//4) * lvl / 100) + 5
        self.dfn = ((dfn * 2 + iv + evs['df']//4) * lvl / 100) + 5
        self.spA = ((spA * 2 + iv + evs['sa']//4) * lvl / 100) + 5
        self.spD = ((spD * 2 + iv + evs['sd']//4) * lvl / 100) + 5
        self.spe = ((spe * 2 + iv + evs['sp']//4) * lvl / 100) + 5
        self.mHP = ((mHP * 2 + iv + evs['hp']//4) * lvl / 100) + 10 + lvl
        if name.lower() == 'shedinja':
            self.mHP = 1
        self.cHP = cHP / 100 * self.mHP
        STATS = {
            'at': self.att,
            'df': self.dfn,
            'sa': self.spA,
            'sd': self.spD,
            'sp': self.spe
        }
        stat_boost = NATURES[nature][0]
        stat_drop = NATURES[nature][1]
        if stat_boost:
            STATS[stat_boost] = STATS[stat_boost] * 1.1
            STATS[stat_drop] = STATS[stat_drop] * 0.9

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
            '\n Item: ' + self.item + \
            '\n' + self.format_evs() + \
            '\n================'

    def format_evs(self):
        for ev, ev_value in self.evs.items():
            print '\n Ev ' + ev + ': ' + str(ev_value)
        return ""


class Move:
    def __init__(self,
        name, type, cat, pow, acc, eff, pp):
        """
            name: 'Tackle'
            type: 'Normal'
            cat: Category {Physical, Special, or Status(not damage dealing)} (ex: Physical)
            pow: Power (ex: 50)
            acc: Accuracy up to 100 (ex: 100)
            eff: Optional Effect Text to be implemented later (ex: <blank> b/c no text)
            pp: How many times can use
        """
        # assign instance variables for each of the traits
        self.name = name
        self.type = type
        self.cat = cat
        self.pow = pow
        self.acc = acc
        self.eff = eff
        self.pp = pp

    def __str__(self):
        """get a printout of all move's info"""

        return '================' + '\n' + self.name.upper() + \
            '\n Type: ' + self.type + \
            '\n Category: ' + self.cat + \
            '\n Power: ' + str(self.pow) + \
            '\n Accuracy: ' + str(self.acc) + \
            '\n Effect: ' + self.eff + \
            '\n PP: ' + str(self.pp) + \
            '\n================'

