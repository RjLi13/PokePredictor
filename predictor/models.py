# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Abilities(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)
    generation = models.ForeignKey('Generations', models.DO_NOTHING)
    is_main_series = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'abilities'


class AbilityChangelog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ability = models.ForeignKey(Abilities, models.DO_NOTHING)
    changed_in_version_group = models.ForeignKey('VersionGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ability_changelog'


class AbilityChangelogProse(models.Model):
    ability_changelog = models.ForeignKey(AbilityChangelog, models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    effect = models.TextField()

    class Meta:
        managed = False
        db_table = 'ability_changelog_prose'
        unique_together = (('ability_changelog', 'local_language'),)


class AbilityFlavorText(models.Model):
    ability = models.ForeignKey(Abilities, models.DO_NOTHING, primary_key=True)
    version_group = models.ForeignKey('VersionGroups', models.DO_NOTHING, primary_key=True)
    language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    flavor_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'ability_flavor_text'
        unique_together = (('ability', 'version_group', 'language'),)


class AbilityNames(models.Model):
    ability = models.ForeignKey(Abilities, models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'ability_names'
        unique_together = (('ability', 'local_language'),)


class AbilityProse(models.Model):
    ability = models.ForeignKey(Abilities, models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    short_effect = models.TextField(blank=True, null=True)
    effect = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ability_prose'
        unique_together = (('ability', 'local_language'),)


class Berries(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    item = models.ForeignKey('Items', models.DO_NOTHING)
    firmness = models.ForeignKey('BerryFirmness', models.DO_NOTHING)
    natural_gift_power = models.IntegerField(blank=True, null=True)
    natural_gift_type = models.ForeignKey('Types', models.DO_NOTHING, blank=True, null=True)
    size = models.IntegerField()
    max_harvest = models.IntegerField()
    growth_time = models.IntegerField()
    soil_dryness = models.IntegerField()
    smoothness = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'berries'


class BerryFirmness(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'berry_firmness'


class BerryFirmnessNames(models.Model):
    berry_firmness = models.ForeignKey(BerryFirmness, models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'berry_firmness_names'
        unique_together = (('berry_firmness', 'local_language'),)


class BerryFlavors(models.Model):
    berry = models.ForeignKey(Berries, models.DO_NOTHING, primary_key=True)
    contest_type = models.ForeignKey('ContestTypes', models.DO_NOTHING, primary_key=True)
    flavor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'berry_flavors'
        unique_together = (('berry', 'contest_type'),)


class CharacteristicText(models.Model):
    characteristic = models.ForeignKey('Characteristics', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    message = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'characteristic_text'
        unique_together = (('characteristic', 'local_language'),)


class Characteristics(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    stat = models.ForeignKey('Stats', models.DO_NOTHING)
    gene_mod_5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'characteristics'


class ConquestEpisodeNames(models.Model):
    episode = models.ForeignKey('ConquestEpisodes', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'conquest_episode_names'
        unique_together = (('episode', 'local_language'),)


class ConquestEpisodeWarriors(models.Model):
    episode = models.ForeignKey('ConquestEpisodes', models.DO_NOTHING, primary_key=True)
    warrior = models.ForeignKey('ConquestWarriors', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'conquest_episode_warriors'
        unique_together = (('episode', 'warrior'),)


class ConquestEpisodes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'conquest_episodes'


class ConquestKingdomNames(models.Model):
    kingdom = models.ForeignKey('ConquestKingdoms', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'conquest_kingdom_names'
        unique_together = (('kingdom', 'local_language'),)


class ConquestKingdoms(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)
    type = models.ForeignKey('Types', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'conquest_kingdoms'


class ConquestMaxLinks(models.Model):
    warrior_rank = models.ForeignKey('ConquestWarriorRanks', models.DO_NOTHING, primary_key=True)
    pokemon_species = models.ForeignKey('PokemonSpecies', models.DO_NOTHING, primary_key=True)
    max_link = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conquest_max_links'
        unique_together = (('warrior_rank', 'pokemon_species'),)


class ConquestMoveData(models.Model):
    move = models.ForeignKey('Moves', models.DO_NOTHING, primary_key=True)
    power = models.IntegerField(blank=True, null=True)
    accuracy = models.IntegerField(blank=True, null=True)
    effect_chance = models.IntegerField(blank=True, null=True)
    effect = models.ForeignKey('ConquestMoveEffects', models.DO_NOTHING)
    range = models.ForeignKey('ConquestMoveRanges', models.DO_NOTHING)
    displacement = models.ForeignKey('ConquestMoveDisplacements', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conquest_move_data'


class ConquestMoveDisplacementProse(models.Model):
    move_displacement = models.ForeignKey('ConquestMoveDisplacements', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79, blank=True, null=True)
    short_effect = models.TextField(blank=True, null=True)
    effect = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conquest_move_displacement_prose'
        unique_together = (('move_displacement', 'local_language'),)


class ConquestMoveDisplacements(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)
    affects_target = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'conquest_move_displacements'


class ConquestMoveEffectProse(models.Model):
    conquest_move_effect = models.ForeignKey('ConquestMoveEffects', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    short_effect = models.TextField(blank=True, null=True)
    effect = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conquest_move_effect_prose'
        unique_together = (('conquest_move_effect', 'local_language'),)


class ConquestMoveEffects(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?

    class Meta:
        managed = False
        db_table = 'conquest_move_effects'


class ConquestMoveRangeProse(models.Model):
    conquest_move_range = models.ForeignKey('ConquestMoveRanges', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conquest_move_range_prose'
        unique_together = (('conquest_move_range', 'local_language'),)


class ConquestMoveRanges(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)
    targets = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conquest_move_ranges'


class ConquestPokemonAbilities(models.Model):
    pokemon_species = models.ForeignKey('PokemonSpecies', models.DO_NOTHING, primary_key=True)
    slot = models.IntegerField(primary_key=True)
    ability = models.ForeignKey(Abilities, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'conquest_pokemon_abilities'
        unique_together = (('pokemon_species', 'slot'),)


class ConquestPokemonEvolution(models.Model):
    evolved_species = models.ForeignKey('PokemonSpecies', models.DO_NOTHING, primary_key=True)
    required_stat = models.ForeignKey('ConquestStats', models.DO_NOTHING, blank=True, null=True)
    minimum_stat = models.IntegerField(blank=True, null=True)
    minimum_link = models.IntegerField(blank=True, null=True)
    kingdom = models.ForeignKey(ConquestKingdoms, models.DO_NOTHING, blank=True, null=True)
    warrior_gender = models.ForeignKey('Genders', models.DO_NOTHING, blank=True, null=True)
    item = models.ForeignKey('Items', models.DO_NOTHING, blank=True, null=True)
    recruiting_ko_required = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'conquest_pokemon_evolution'


class ConquestPokemonMoves(models.Model):
    pokemon_species = models.ForeignKey('PokemonSpecies', models.DO_NOTHING, primary_key=True)
    move = models.ForeignKey('Moves', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'conquest_pokemon_moves'


class ConquestPokemonStats(models.Model):
    pokemon_species = models.ForeignKey('PokemonSpecies', models.DO_NOTHING, primary_key=True)
    conquest_stat = models.ForeignKey('ConquestStats', models.DO_NOTHING, primary_key=True)
    base_stat = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conquest_pokemon_stats'
        unique_together = (('pokemon_species', 'conquest_stat'),)


class ConquestStatNames(models.Model):
    conquest_stat = models.ForeignKey('ConquestStats', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'conquest_stat_names'
        unique_together = (('conquest_stat', 'local_language'),)


class ConquestStats(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)
    is_base = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'conquest_stats'


class ConquestTransformationPokemon(models.Model):
    transformation = models.ForeignKey('ConquestWarriorTransformation', models.DO_NOTHING, primary_key=True)
    pokemon_species = models.ForeignKey('PokemonSpecies', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'conquest_transformation_pokemon'
        unique_together = (('transformation', 'pokemon_species'),)


class ConquestTransformationWarriors(models.Model):
    transformation = models.ForeignKey('ConquestWarriorTransformation', models.DO_NOTHING, primary_key=True)
    present_warrior = models.ForeignKey('ConquestWarriors', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'conquest_transformation_warriors'
        unique_together = (('transformation', 'present_warrior'),)


class ConquestWarriorArchetypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'conquest_warrior_archetypes'


class ConquestWarriorNames(models.Model):
    warrior = models.ForeignKey('ConquestWarriors', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'conquest_warrior_names'
        unique_together = (('warrior', 'local_language'),)


class ConquestWarriorRankStatMap(models.Model):
    warrior_rank = models.ForeignKey('ConquestWarriorRanks', models.DO_NOTHING, primary_key=True)
    warrior_stat = models.ForeignKey('ConquestWarriorStats', models.DO_NOTHING, primary_key=True)
    base_stat = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conquest_warrior_rank_stat_map'
        unique_together = (('warrior_rank', 'warrior_stat'),)


class ConquestWarriorRanks(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    warrior = models.ForeignKey('ConquestWarriors', models.DO_NOTHING)
    rank = models.IntegerField()
    skill = models.ForeignKey('ConquestWarriorSkills', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'conquest_warrior_ranks'
        unique_together = (('warrior', 'rank'),)


class ConquestWarriorSkillNames(models.Model):
    skill = models.ForeignKey('ConquestWarriorSkills', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'conquest_warrior_skill_names'
        unique_together = (('skill', 'local_language'),)


class ConquestWarriorSkills(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'conquest_warrior_skills'


class ConquestWarriorSpecialties(models.Model):
    warrior = models.ForeignKey('ConquestWarriors', models.DO_NOTHING, primary_key=True)
    type = models.ForeignKey('Types', models.DO_NOTHING, primary_key=True)
    slot = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'conquest_warrior_specialties'
        unique_together = (('warrior', 'type', 'slot'),)


class ConquestWarriorStatNames(models.Model):
    warrior_stat = models.ForeignKey('ConquestWarriorStats', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'conquest_warrior_stat_names'
        unique_together = (('warrior_stat', 'local_language'),)


class ConquestWarriorStats(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'conquest_warrior_stats'


class ConquestWarriorTransformation(models.Model):
    transformed_warrior_rank = models.ForeignKey(ConquestWarriorRanks, models.DO_NOTHING, primary_key=True)
    is_automatic = models.BooleanField()
    required_link = models.IntegerField(blank=True, null=True)
    completed_episode = models.ForeignKey(ConquestEpisodes, models.DO_NOTHING, blank=True, null=True)
    current_episode = models.ForeignKey(ConquestEpisodes, models.DO_NOTHING, blank=True, null=True)
    distant_warrior = models.ForeignKey('ConquestWarriors', models.DO_NOTHING, blank=True, null=True)
    female_warlord_count = models.IntegerField(blank=True, null=True)
    pokemon_count = models.IntegerField(blank=True, null=True)
    collection_type = models.ForeignKey('Types', models.DO_NOTHING, blank=True, null=True)
    warrior_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conquest_warrior_transformation'


class ConquestWarriors(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)
    gender = models.ForeignKey('Genders', models.DO_NOTHING)
    archetype = models.ForeignKey(ConquestWarriorArchetypes, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conquest_warriors'


class ContestCombos(models.Model):
    first_move = models.ForeignKey('Moves', models.DO_NOTHING, primary_key=True)
    second_move = models.ForeignKey('Moves', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'contest_combos'
        unique_together = (('first_move', 'second_move'),)


class ContestEffectProse(models.Model):
    contest_effect = models.ForeignKey('ContestEffects', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    flavor_text = models.TextField(blank=True, null=True)
    effect = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contest_effect_prose'
        unique_together = (('contest_effect', 'local_language'),)


class ContestEffects(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    appeal = models.SmallIntegerField()
    jam = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'contest_effects'


class ContestTypeNames(models.Model):
    contest_type = models.ForeignKey('ContestTypes', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79, blank=True, null=True)
    flavor = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contest_type_names'
        unique_together = (('contest_type', 'local_language'),)


class ContestTypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'contest_types'


class EggGroupProse(models.Model):
    egg_group = models.ForeignKey('EggGroups', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'egg_group_prose'
        unique_together = (('egg_group', 'local_language'),)


class EggGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'egg_groups'


class EncounterConditionProse(models.Model):
    encounter_condition = models.ForeignKey('EncounterConditions', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'encounter_condition_prose'
        unique_together = (('encounter_condition', 'local_language'),)


class EncounterConditionValueMap(models.Model):
    encounter = models.ForeignKey('Encounters', models.DO_NOTHING, primary_key=True)
    encounter_condition_value = models.ForeignKey('EncounterConditionValues', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'encounter_condition_value_map'
        unique_together = (('encounter', 'encounter_condition_value'),)


class EncounterConditionValueProse(models.Model):
    encounter_condition_value = models.ForeignKey('EncounterConditionValues', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'encounter_condition_value_prose'
        unique_together = (('encounter_condition_value', 'local_language'),)


class EncounterConditionValues(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    encounter_condition = models.ForeignKey('EncounterConditions', models.DO_NOTHING)
    identifier = models.CharField(max_length=79)
    is_default = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'encounter_condition_values'


class EncounterConditions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'encounter_conditions'


class EncounterMethodProse(models.Model):
    encounter_method = models.ForeignKey('EncounterMethods', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'encounter_method_prose'
        unique_together = (('encounter_method', 'local_language'),)


class EncounterMethods(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(unique=True, max_length=79)
    order = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'encounter_methods'


class EncounterSlots(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    version_group = models.ForeignKey('VersionGroups', models.DO_NOTHING)
    encounter_method = models.ForeignKey(EncounterMethods, models.DO_NOTHING)
    slot = models.IntegerField(blank=True, null=True)
    rarity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'encounter_slots'


class Encounters(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    version = models.ForeignKey('Versions', models.DO_NOTHING)
    location_area = models.ForeignKey('LocationAreas', models.DO_NOTHING)
    encounter_slot = models.ForeignKey(EncounterSlots, models.DO_NOTHING)
    pokemon = models.ForeignKey('Pokemon', models.DO_NOTHING)
    min_level = models.IntegerField()
    max_level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'encounters'


class EvolutionChains(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    baby_trigger_item = models.ForeignKey('Items', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evolution_chains'


class EvolutionTriggerProse(models.Model):
    evolution_trigger = models.ForeignKey('EvolutionTriggers', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'evolution_trigger_prose'
        unique_together = (('evolution_trigger', 'local_language'),)


class EvolutionTriggers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'evolution_triggers'


class Experience(models.Model):
    growth_rate = models.ForeignKey('GrowthRates', models.DO_NOTHING, primary_key=True)
    level = models.IntegerField(primary_key=True)
    experience = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'experience'
        unique_together = (('growth_rate', 'level'),)


class Genders(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'genders'


class GenerationNames(models.Model):
    generation = models.ForeignKey('Generations', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'generation_names'
        unique_together = (('generation', 'local_language'),)


class Generations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    main_region = models.ForeignKey('Regions', models.DO_NOTHING)
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'generations'


class GrowthRateProse(models.Model):
    growth_rate = models.ForeignKey('GrowthRates', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'growth_rate_prose'
        unique_together = (('growth_rate', 'local_language'),)


class GrowthRates(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)
    formula = models.TextField()

    class Meta:
        managed = False
        db_table = 'growth_rates'


class ItemCategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    pocket = models.ForeignKey('ItemPockets', models.DO_NOTHING)
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'item_categories'


class ItemCategoryProse(models.Model):
    item_category = models.ForeignKey(ItemCategories, models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'item_category_prose'
        unique_together = (('item_category', 'local_language'),)


class ItemFlagMap(models.Model):
    item = models.ForeignKey('Items', models.DO_NOTHING, primary_key=True)
    item_flag = models.ForeignKey('ItemFlags', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'item_flag_map'
        unique_together = (('item', 'item_flag'),)


class ItemFlagProse(models.Model):
    item_flag = models.ForeignKey('ItemFlags', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_flag_prose'
        unique_together = (('item_flag', 'local_language'),)


class ItemFlags(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'item_flags'


class ItemFlavorSummaries(models.Model):
    item = models.ForeignKey('Items', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    flavor_summary = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_flavor_summaries'
        unique_together = (('item', 'local_language'),)


class ItemFlavorText(models.Model):
    item = models.ForeignKey('Items', models.DO_NOTHING, primary_key=True)
    version_group = models.ForeignKey('VersionGroups', models.DO_NOTHING, primary_key=True)
    language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    flavor_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'item_flavor_text'
        unique_together = (('item', 'version_group', 'language'),)


class ItemFlingEffectProse(models.Model):
    item_fling_effect = models.ForeignKey('ItemFlingEffects', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    effect = models.TextField()

    class Meta:
        managed = False
        db_table = 'item_fling_effect_prose'
        unique_together = (('item_fling_effect', 'local_language'),)


class ItemFlingEffects(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?

    class Meta:
        managed = False
        db_table = 'item_fling_effects'


class ItemGameIndices(models.Model):
    item = models.ForeignKey('Items', models.DO_NOTHING, primary_key=True)
    generation = models.ForeignKey(Generations, models.DO_NOTHING, primary_key=True)
    game_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'item_game_indices'
        unique_together = (('item', 'generation'),)


class ItemNames(models.Model):
    item = models.ForeignKey('Items', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'item_names'
        unique_together = (('item', 'local_language'),)


class ItemPocketNames(models.Model):
    item_pocket = models.ForeignKey('ItemPockets', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'item_pocket_names'
        unique_together = (('item_pocket', 'local_language'),)


class ItemPockets(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'item_pockets'


class ItemProse(models.Model):
    item = models.ForeignKey('Items', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    short_effect = models.TextField(blank=True, null=True)
    effect = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_prose'
        unique_together = (('item', 'local_language'),)


class Items(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)
    category = models.ForeignKey(ItemCategories, models.DO_NOTHING)
    cost = models.IntegerField()
    fling_power = models.IntegerField(blank=True, null=True)
    fling_effect = models.ForeignKey(ItemFlingEffects, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'


class LanguageNames(models.Model):
    language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey('Languages', models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'language_names'
        unique_together = (('language', 'local_language'),)


class Languages(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    iso639 = models.CharField(max_length=79)
    iso3166 = models.CharField(max_length=79)
    identifier = models.CharField(max_length=79)
    official = models.BooleanField()
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'languages'


class LocationAreaEncounterRates(models.Model):
    location_area = models.ForeignKey('LocationAreas', models.DO_NOTHING, primary_key=True)
    encounter_method = models.ForeignKey(EncounterMethods, models.DO_NOTHING, primary_key=True)
    version = models.ForeignKey('Versions', models.DO_NOTHING, primary_key=True)
    rate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location_area_encounter_rates'
        unique_together = (('location_area', 'encounter_method', 'version'),)


class LocationAreaProse(models.Model):
    location_area = models.ForeignKey('LocationAreas', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location_area_prose'
        unique_together = (('location_area', 'local_language'),)


class LocationAreas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    location = models.ForeignKey('Locations', models.DO_NOTHING)
    game_index = models.IntegerField()
    identifier = models.CharField(max_length=79, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location_areas'


class LocationGameIndices(models.Model):
    location = models.ForeignKey('Locations', models.DO_NOTHING, primary_key=True)
    generation = models.ForeignKey(Generations, models.DO_NOTHING, primary_key=True)
    game_index = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'location_game_indices'
        unique_together = (('location', 'generation', 'game_index'),)


class LocationNames(models.Model):
    location = models.ForeignKey('Locations', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'location_names'
        unique_together = (('location', 'local_language'),)


class Locations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    region = models.ForeignKey('Regions', models.DO_NOTHING, blank=True, null=True)
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'locations'


class Machines(models.Model):
    machine_number = models.IntegerField(primary_key=True)
    version_group = models.ForeignKey('VersionGroups', models.DO_NOTHING, primary_key=True)
    item = models.ForeignKey(Items, models.DO_NOTHING)
    move = models.ForeignKey('Moves', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'machines'
        unique_together = (('machine_number', 'version_group'),)


class MoveBattleStyleProse(models.Model):
    move_battle_style = models.ForeignKey('MoveBattleStyles', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'move_battle_style_prose'
        unique_together = (('move_battle_style', 'local_language'),)


class MoveBattleStyles(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'move_battle_styles'


class MoveChangelog(models.Model):
    move = models.ForeignKey('Moves', models.DO_NOTHING, primary_key=True)
    changed_in_version_group = models.ForeignKey('VersionGroups', models.DO_NOTHING, primary_key=True)
    type = models.ForeignKey('Types', models.DO_NOTHING, blank=True, null=True)
    power = models.SmallIntegerField(blank=True, null=True)
    pp = models.SmallIntegerField(blank=True, null=True)
    accuracy = models.SmallIntegerField(blank=True, null=True)
    effect = models.ForeignKey('MoveEffects', models.DO_NOTHING, blank=True, null=True)
    effect_chance = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'move_changelog'
        unique_together = (('move', 'changed_in_version_group'),)


class MoveDamageClassProse(models.Model):
    move_damage_class = models.ForeignKey('MoveDamageClasses', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'move_damage_class_prose'
        unique_together = (('move_damage_class', 'local_language'),)


class MoveDamageClasses(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'move_damage_classes'


class MoveEffectChangelog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    effect = models.ForeignKey('MoveEffects', models.DO_NOTHING)
    changed_in_version_group = models.ForeignKey('VersionGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'move_effect_changelog'
        unique_together = (('effect', 'changed_in_version_group'),)


class MoveEffectChangelogProse(models.Model):
    move_effect_changelog = models.ForeignKey(MoveEffectChangelog, models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    effect = models.TextField()

    class Meta:
        managed = False
        db_table = 'move_effect_changelog_prose'
        unique_together = (('move_effect_changelog', 'local_language'),)


class MoveEffectProse(models.Model):
    move_effect = models.ForeignKey('MoveEffects', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    short_effect = models.TextField(blank=True, null=True)
    effect = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'move_effect_prose'
        unique_together = (('move_effect', 'local_language'),)


class MoveEffects(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?

    class Meta:
        managed = False
        db_table = 'move_effects'


class MoveFlagMap(models.Model):
    move = models.ForeignKey('Moves', models.DO_NOTHING, primary_key=True)
    move_flag = models.ForeignKey('MoveFlags', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'move_flag_map'
        unique_together = (('move', 'move_flag'),)


class MoveFlagProse(models.Model):
    move_flag = models.ForeignKey('MoveFlags', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'move_flag_prose'
        unique_together = (('move_flag', 'local_language'),)


class MoveFlags(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'move_flags'


class MoveFlavorSummaries(models.Model):
    move = models.ForeignKey('Moves', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    flavor_summary = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'move_flavor_summaries'
        unique_together = (('move', 'local_language'),)


class MoveFlavorText(models.Model):
    move = models.ForeignKey('Moves', models.DO_NOTHING, primary_key=True)
    version_group = models.ForeignKey('VersionGroups', models.DO_NOTHING, primary_key=True)
    language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    flavor_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'move_flavor_text'
        unique_together = (('move', 'version_group', 'language'),)


class MoveMeta(models.Model):
    move = models.ForeignKey('Moves', models.DO_NOTHING, primary_key=True)
    meta_category = models.ForeignKey('MoveMetaCategories', models.DO_NOTHING)
    meta_ailment = models.ForeignKey('MoveMetaAilments', models.DO_NOTHING)
    min_hits = models.IntegerField(blank=True, null=True)
    max_hits = models.IntegerField(blank=True, null=True)
    min_turns = models.IntegerField(blank=True, null=True)
    max_turns = models.IntegerField(blank=True, null=True)
    drain = models.IntegerField()
    healing = models.IntegerField()
    crit_rate = models.IntegerField()
    ailment_chance = models.IntegerField()
    flinch_chance = models.IntegerField()
    stat_chance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'move_meta'


class MoveMetaAilmentNames(models.Model):
    move_meta_ailment = models.ForeignKey('MoveMetaAilments', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'move_meta_ailment_names'
        unique_together = (('move_meta_ailment', 'local_language'),)


class MoveMetaAilments(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(unique=True, max_length=79)

    class Meta:
        managed = False
        db_table = 'move_meta_ailments'


class MoveMetaCategories(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(unique=True, max_length=79)

    class Meta:
        managed = False
        db_table = 'move_meta_categories'


class MoveMetaCategoryProse(models.Model):
    move_meta_category = models.ForeignKey(MoveMetaCategories, models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'move_meta_category_prose'
        unique_together = (('move_meta_category', 'local_language'),)


class MoveMetaStatChanges(models.Model):
    move = models.ForeignKey('Moves', models.DO_NOTHING, primary_key=True)
    stat = models.ForeignKey('Stats', models.DO_NOTHING, primary_key=True)
    change = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'move_meta_stat_changes'
        unique_together = (('move', 'stat'),)


class MoveNames(models.Model):
    move = models.ForeignKey('Moves', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'move_names'
        unique_together = (('move', 'local_language'),)


class MoveTargetProse(models.Model):
    move_target = models.ForeignKey('MoveTargets', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'move_target_prose'
        unique_together = (('move_target', 'local_language'),)


class MoveTargets(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'move_targets'


class Moves(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)
    generation = models.ForeignKey(Generations, models.DO_NOTHING)
    type = models.ForeignKey('Types', models.DO_NOTHING)
    power = models.SmallIntegerField(blank=True, null=True)
    pp = models.SmallIntegerField(blank=True, null=True)
    accuracy = models.SmallIntegerField(blank=True, null=True)
    priority = models.SmallIntegerField()
    target = models.ForeignKey(MoveTargets, models.DO_NOTHING)
    damage_class = models.ForeignKey(MoveDamageClasses, models.DO_NOTHING)
    effect = models.ForeignKey(MoveEffects, models.DO_NOTHING)
    effect_chance = models.IntegerField(blank=True, null=True)
    contest_type = models.ForeignKey(ContestTypes, models.DO_NOTHING, blank=True, null=True)
    contest_effect = models.ForeignKey(ContestEffects, models.DO_NOTHING, blank=True, null=True)
    super_contest_effect = models.ForeignKey('SuperContestEffects', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moves'


class NatureBattleStylePreferences(models.Model):
    nature = models.ForeignKey('Natures', models.DO_NOTHING, primary_key=True)
    move_battle_style = models.ForeignKey(MoveBattleStyles, models.DO_NOTHING, primary_key=True)
    low_hp_preference = models.IntegerField()
    high_hp_preference = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nature_battle_style_preferences'
        unique_together = (('nature', 'move_battle_style'),)


class NatureNames(models.Model):
    nature = models.ForeignKey('Natures', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'nature_names'
        unique_together = (('nature', 'local_language'),)


class NaturePokeathlonStats(models.Model):
    nature = models.ForeignKey('Natures', models.DO_NOTHING, primary_key=True)
    pokeathlon_stat = models.ForeignKey('PokeathlonStats', models.DO_NOTHING, primary_key=True)
    max_change = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nature_pokeathlon_stats'
        unique_together = (('nature', 'pokeathlon_stat'),)


class Natures(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)
    decreased_stat = models.ForeignKey('Stats', models.DO_NOTHING)
    increased_stat = models.ForeignKey('Stats', models.DO_NOTHING)
    hates_flavor = models.ForeignKey(ContestTypes, models.DO_NOTHING)
    likes_flavor = models.ForeignKey(ContestTypes, models.DO_NOTHING)
    game_index = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'natures'


class PalPark(models.Model):
    species = models.ForeignKey('PokemonSpecies', models.DO_NOTHING, primary_key=True)
    area = models.ForeignKey('PalParkAreas', models.DO_NOTHING)
    base_score = models.IntegerField()
    rate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pal_park'


class PalParkAreaNames(models.Model):
    pal_park_area = models.ForeignKey('PalParkAreas', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'pal_park_area_names'
        unique_together = (('pal_park_area', 'local_language'),)


class PalParkAreas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'pal_park_areas'


class PokeathlonStatNames(models.Model):
    pokeathlon_stat = models.ForeignKey('PokeathlonStats', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'pokeathlon_stat_names'
        unique_together = (('pokeathlon_stat', 'local_language'),)


class PokeathlonStats(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'pokeathlon_stats'


class PokedexProse(models.Model):
    pokedex = models.ForeignKey('Pokedexes', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokedex_prose'
        unique_together = (('pokedex', 'local_language'),)


class PokedexVersionGroups(models.Model):
    pokedex = models.ForeignKey('Pokedexes', models.DO_NOTHING, primary_key=True)
    version_group = models.ForeignKey('VersionGroups', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'pokedex_version_groups'
        unique_together = (('pokedex', 'version_group'),)


class Pokedexes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    region = models.ForeignKey('Regions', models.DO_NOTHING, blank=True, null=True)
    identifier = models.CharField(max_length=79)
    is_main_series = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pokedexes'


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)
    species = models.ForeignKey('PokemonSpecies', models.DO_NOTHING, blank=True, null=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    base_experience = models.IntegerField()
    order = models.IntegerField()
    is_default = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pokemon'


class PokemonAbilities(models.Model):
    pokemon = models.ForeignKey(Pokemon, models.DO_NOTHING, primary_key=True)
    ability = models.ForeignKey(Abilities, models.DO_NOTHING)
    is_hidden = models.BooleanField()
    slot = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pokemon_abilities'
        unique_together = (('pokemon', 'slot'),)


class PokemonColorNames(models.Model):
    pokemon_color = models.ForeignKey('PokemonColors', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'pokemon_color_names'
        unique_together = (('pokemon_color', 'local_language'),)


class PokemonColors(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'pokemon_colors'


class PokemonDexNumbers(models.Model):
    species = models.ForeignKey('PokemonSpecies', models.DO_NOTHING, primary_key=True)
    pokedex = models.ForeignKey(Pokedexes, models.DO_NOTHING, primary_key=True)
    pokedex_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_dex_numbers'
        unique_together = (('species', 'pokedex'),)


class PokemonEggGroups(models.Model):
    species = models.ForeignKey('PokemonSpecies', models.DO_NOTHING, primary_key=True)
    egg_group = models.ForeignKey(EggGroups, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'pokemon_egg_groups'
        unique_together = (('species', 'egg_group'),)


class PokemonEvolution(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    evolved_species = models.ForeignKey('PokemonSpecies', models.DO_NOTHING)
    evolution_trigger = models.ForeignKey(EvolutionTriggers, models.DO_NOTHING)
    trigger_item = models.ForeignKey(Items, models.DO_NOTHING, blank=True, null=True)
    minimum_level = models.IntegerField(blank=True, null=True)
    gender = models.ForeignKey(Genders, models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(Locations, models.DO_NOTHING, blank=True, null=True)
    held_item = models.ForeignKey(Items, models.DO_NOTHING, blank=True, null=True)
    time_of_day = models.CharField(max_length=5, blank=True, null=True)
    known_move = models.ForeignKey(Moves, models.DO_NOTHING, blank=True, null=True)
    known_move_type = models.ForeignKey('Types', models.DO_NOTHING, blank=True, null=True)
    minimum_happiness = models.IntegerField(blank=True, null=True)
    minimum_beauty = models.IntegerField(blank=True, null=True)
    minimum_affection = models.IntegerField(blank=True, null=True)
    relative_physical_stats = models.IntegerField(blank=True, null=True)
    party_species = models.ForeignKey('PokemonSpecies', models.DO_NOTHING, blank=True, null=True)
    party_type = models.ForeignKey('Types', models.DO_NOTHING, blank=True, null=True)
    trade_species = models.ForeignKey('PokemonSpecies', models.DO_NOTHING, blank=True, null=True)
    needs_overworld_rain = models.BooleanField()
    turn_upside_down = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pokemon_evolution'


class PokemonFormGenerations(models.Model):
    pokemon_form = models.ForeignKey('PokemonForms', models.DO_NOTHING, primary_key=True)
    generation = models.ForeignKey(Generations, models.DO_NOTHING, primary_key=True)
    game_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_form_generations'
        unique_together = (('pokemon_form', 'generation'),)


class PokemonFormNames(models.Model):
    pokemon_form = models.ForeignKey('PokemonForms', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    form_name = models.CharField(max_length=79, blank=True, null=True)
    pokemon_name = models.CharField(max_length=79, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_form_names'
        unique_together = (('pokemon_form', 'local_language'),)


class PokemonFormPokeathlonStats(models.Model):
    pokemon_form = models.ForeignKey('PokemonForms', models.DO_NOTHING, primary_key=True)
    pokeathlon_stat = models.ForeignKey(PokeathlonStats, models.DO_NOTHING, primary_key=True)
    minimum_stat = models.IntegerField()
    base_stat = models.IntegerField()
    maximum_stat = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_form_pokeathlon_stats'
        unique_together = (('pokemon_form', 'pokeathlon_stat'),)


class PokemonForms(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)
    form_identifier = models.CharField(max_length=79, blank=True, null=True)
    pokemon = models.ForeignKey(Pokemon, models.DO_NOTHING)
    introduced_in_version_group = models.ForeignKey('VersionGroups', models.DO_NOTHING, blank=True, null=True)
    is_default = models.BooleanField()
    is_battle_only = models.BooleanField()
    is_mega = models.BooleanField()
    form_order = models.IntegerField()
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_forms'


class PokemonGameIndices(models.Model):
    pokemon = models.ForeignKey(Pokemon, models.DO_NOTHING, primary_key=True)
    version = models.ForeignKey('Versions', models.DO_NOTHING, primary_key=True)
    game_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_game_indices'
        unique_together = (('pokemon', 'version'),)


class PokemonHabitatNames(models.Model):
    pokemon_habitat = models.ForeignKey('PokemonHabitats', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'pokemon_habitat_names'
        unique_together = (('pokemon_habitat', 'local_language'),)


class PokemonHabitats(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'pokemon_habitats'


class PokemonItems(models.Model):
    pokemon = models.ForeignKey(Pokemon, models.DO_NOTHING, primary_key=True)
    version = models.ForeignKey('Versions', models.DO_NOTHING, primary_key=True)
    item = models.ForeignKey(Items, models.DO_NOTHING, primary_key=True)
    rarity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_items'
        unique_together = (('pokemon', 'version', 'item'),)


class PokemonMoveMethodProse(models.Model):
    pokemon_move_method = models.ForeignKey('PokemonMoveMethods', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_move_method_prose'
        unique_together = (('pokemon_move_method', 'local_language'),)


class PokemonMoveMethods(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'pokemon_move_methods'


class PokemonMoves(models.Model):
    pokemon = models.ForeignKey(Pokemon, models.DO_NOTHING, primary_key=True)
    version_group = models.ForeignKey('VersionGroups', models.DO_NOTHING, primary_key=True)
    move = models.ForeignKey(Moves, models.DO_NOTHING, primary_key=True)
    pokemon_move_method = models.ForeignKey(PokemonMoveMethods, models.DO_NOTHING, primary_key=True)
    level = models.IntegerField(primary_key=True)
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_moves'
        unique_together = (('pokemon', 'version_group', 'move', 'pokemon_move_method', 'level'),)


class PokemonShapeProse(models.Model):
    pokemon_shape = models.ForeignKey('PokemonShapes', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79, blank=True, null=True)
    awesome_name = models.CharField(max_length=79, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_shape_prose'
        unique_together = (('pokemon_shape', 'local_language'),)


class PokemonShapes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'pokemon_shapes'


class PokemonSpecies(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)
    generation = models.ForeignKey(Generations, models.DO_NOTHING, blank=True, null=True)
    evolves_from_species = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    evolution_chain = models.ForeignKey(EvolutionChains, models.DO_NOTHING, blank=True, null=True)
    color = models.ForeignKey(PokemonColors, models.DO_NOTHING)
    shape = models.ForeignKey(PokemonShapes, models.DO_NOTHING)
    habitat = models.ForeignKey(PokemonHabitats, models.DO_NOTHING, blank=True, null=True)
    gender_rate = models.IntegerField()
    capture_rate = models.IntegerField()
    base_happiness = models.IntegerField()
    is_baby = models.BooleanField()
    hatch_counter = models.IntegerField()
    has_gender_differences = models.BooleanField()
    growth_rate = models.ForeignKey(GrowthRates, models.DO_NOTHING)
    forms_switchable = models.BooleanField()
    order = models.IntegerField()
    conquest_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_species'


class PokemonSpeciesFlavorSummaries(models.Model):
    pokemon_species = models.ForeignKey(PokemonSpecies, models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    flavor_summary = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_species_flavor_summaries'
        unique_together = (('pokemon_species', 'local_language'),)


class PokemonSpeciesFlavorText(models.Model):
    species = models.ForeignKey(PokemonSpecies, models.DO_NOTHING, primary_key=True)
    version = models.ForeignKey('Versions', models.DO_NOTHING, primary_key=True)
    language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    flavor_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'pokemon_species_flavor_text'
        unique_together = (('species', 'version', 'language'),)


class PokemonSpeciesNames(models.Model):
    pokemon_species = models.ForeignKey(PokemonSpecies, models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79, blank=True, null=True)
    genus = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_species_names'
        unique_together = (('pokemon_species', 'local_language'),)


class PokemonSpeciesProse(models.Model):
    pokemon_species = models.ForeignKey(PokemonSpecies, models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    form_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pokemon_species_prose'
        unique_together = (('pokemon_species', 'local_language'),)


class PokemonStats(models.Model):
    pokemon = models.ForeignKey(Pokemon, models.DO_NOTHING, primary_key=True)
    stat = models.ForeignKey('Stats', models.DO_NOTHING, primary_key=True)
    base_stat = models.IntegerField()
    effort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pokemon_stats'
        unique_together = (('pokemon', 'stat'),)


class PokemonTypes(models.Model):
    pokemon = models.ForeignKey(Pokemon, models.DO_NOTHING, primary_key=True)
    type = models.ForeignKey('Types', models.DO_NOTHING)
    slot = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pokemon_types'
        unique_together = (('pokemon', 'slot'),)


class RegionNames(models.Model):
    region = models.ForeignKey('Regions', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'region_names'
        unique_together = (('region', 'local_language'),)


class Regions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'regions'


class StatNames(models.Model):
    stat = models.ForeignKey('Stats', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'stat_names'
        unique_together = (('stat', 'local_language'),)


class Stats(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    damage_class = models.ForeignKey(MoveDamageClasses, models.DO_NOTHING, blank=True, null=True)
    identifier = models.CharField(max_length=79)
    is_battle_only = models.BooleanField()
    game_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stats'


class SuperContestCombos(models.Model):
    first_move = models.ForeignKey(Moves, models.DO_NOTHING, primary_key=True)
    second_move = models.ForeignKey(Moves, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'super_contest_combos'
        unique_together = (('first_move', 'second_move'),)


class SuperContestEffectProse(models.Model):
    super_contest_effect = models.ForeignKey('SuperContestEffects', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    flavor_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'super_contest_effect_prose'
        unique_together = (('super_contest_effect', 'local_language'),)


class SuperContestEffects(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    appeal = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'super_contest_effects'


class TypeEfficacy(models.Model):
    damage_type = models.ForeignKey('Types', models.DO_NOTHING, primary_key=True)
    target_type = models.ForeignKey('Types', models.DO_NOTHING, primary_key=True)
    damage_factor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'type_efficacy'
        unique_together = (('damage_type', 'target_type'),)


class TypeGameIndices(models.Model):
    type = models.ForeignKey('Types', models.DO_NOTHING, primary_key=True)
    generation = models.ForeignKey(Generations, models.DO_NOTHING, primary_key=True)
    game_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'type_game_indices'
        unique_together = (('type', 'generation'),)


class TypeNames(models.Model):
    type = models.ForeignKey('Types', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'type_names'
        unique_together = (('type', 'local_language'),)


class Types(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(max_length=79)
    generation = models.ForeignKey(Generations, models.DO_NOTHING)
    damage_class = models.ForeignKey(MoveDamageClasses, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'types'


class VersionGroupPokemonMoveMethods(models.Model):
    version_group = models.ForeignKey('VersionGroups', models.DO_NOTHING, primary_key=True)
    pokemon_move_method = models.ForeignKey(PokemonMoveMethods, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'version_group_pokemon_move_methods'
        unique_together = (('version_group', 'pokemon_move_method'),)


class VersionGroupRegions(models.Model):
    version_group = models.ForeignKey('VersionGroups', models.DO_NOTHING, primary_key=True)
    region = models.ForeignKey(Regions, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'version_group_regions'
        unique_together = (('version_group', 'region'),)


class VersionGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identifier = models.CharField(unique=True, max_length=79)
    generation = models.ForeignKey(Generations, models.DO_NOTHING)
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'version_groups'


class VersionNames(models.Model):
    version = models.ForeignKey('Versions', models.DO_NOTHING, primary_key=True)
    local_language = models.ForeignKey(Languages, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'version_names'
        unique_together = (('version', 'local_language'),)


class Versions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    version_group = models.ForeignKey(VersionGroups, models.DO_NOTHING)
    identifier = models.CharField(max_length=79)

    class Meta:
        managed = False
        db_table = 'versions'
