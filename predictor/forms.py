__author__ = 'ruijing'
from django import forms

class PokeForm(forms.Form):
    """
    This is a forms class. Its purpose is to take fields characterized by Choice/Text/Ints and display
    those fields to the user in a form. The user enters data into the form, which if filled correctly
    will be stored into a dictionary form.cleaned_data
    """
    nature_choices = [("Adamant", "Adamant"), ("Bashful", "Bashful"), ("Bold", "Bold"), ("Brave", "Brave"),
                      ("Calm", "Calm"), ("Careful", "Careful"), ("Docile", "Docile"), ("Gentle", "Gentle"),
                      ("Hardy", "Hardy"), ("Hasty", "Hasty"), ("Impish", "Impish"), ("Jolly", "Jolly"), ("Lax", "Lax"),
                      ("Lonely", "Lonely"), ("Mild", "Mild"), ("Modest", "Modest"), ("Naive", "Naive"),
                      ("Naughty", "Naughty"), ("Quiet", "Quiet"), ("Quirky", "Quirky"), ("Rash", "Rash"),
                      ("Relaxed", "Relaxed"), ("Sassy", "Sassy"), ("Serious", "Serious"), ("Timid", "Timid")]
    type_choices = [("normal", "normal"), ("fire", "fire"), ("water", "water"), ("electric", "electric"),
                    ("grass", "grass"), ("ice", "ice"), ("fighting", "fighting"), ("poison", "poison"), ("ground", "ground"),
                    ("flying","flying"), ("psychic", "psychic"), ("bug", "bug"), ("rock","rock"),
                    ("ghost", "ghost"), ("dragon", "dragon"), ("dark", "dark"), ("steel", "steel"), ("fairy", "fairy")]
    category_choices = [('Physical', 'Physical'), ('Special', 'Special'), ('Status', 'Status')]
    name = forms.CharField(label='Your Pokemon name', max_length=30)
    nature = forms.ChoiceField(choices=nature_choices, label=' Your Pokemon nature')
    move1 = forms.CharField(label='Your Pokemon move 1', max_length=100)
    move1_type = forms.ChoiceField(choices=type_choices, label='Your Pokemon move 1 type')
    move1_category = forms.ChoiceField(choices=category_choices, label='Your Pokemon move 1 category')
    move2 = forms.CharField(label='Your Pokemon move 2', max_length=100)
    move2_type = forms.ChoiceField(choices=type_choices, label='Your Pokemon move 2 type')
    move2_category = forms.ChoiceField(choices=category_choices, label='Your Pokemon move 2 category')
    move3 = forms.CharField(label='Your Pokemon move 3', max_length=100)
    move3_type = forms.ChoiceField(choices=type_choices, label='Your Pokemon move 3 type')
    move3_category = forms.ChoiceField(choices=category_choices, label='Your Pokemon move 3 category')
    move4 = forms.CharField(label='Your Pokemon move 4', max_length=100)
    move4_type = forms.ChoiceField(choices=type_choices, label='Your Pokemon move 4 type')
    move4_category = forms.ChoiceField(choices=category_choices, label='Your Pokemon move 4 category')
    opp_name = forms.CharField(label='Opponent\'s Pokemon name', max_length=30)
    level = forms.IntegerField(label='Your Pokemon level (Optional)', required=False)
    current_HP = forms.IntegerField(label='Your Pokemon current HP (as percentage %) (Optional)', required=False)
    ev_hp = forms.IntegerField(label='Your Pokemon evs on HP (Optional)', required=False)
    ev_atk = forms.IntegerField(label='Your Pokemon evs on Atk (Optional)', required=False)
    ev_def = forms.IntegerField(label='Your Pokemon evs on Def (Optional)', required=False)
    ev_spatk = forms.IntegerField(label='Your Pokemon evs on Sp Atk (Optional)', required=False)
    ev_spdef = forms.IntegerField(label='Your Pokemon evs on Sp Def (Optional)', required=False)
    ev_speed = forms.IntegerField(label='Your Pokemon evs on Speed (Optional)', required=False)
    num_pokemon = forms.IntegerField(label='How many pokemon left on your team (including this one) (Optional)', required=False)
    ability = forms.CharField(label='Your Pokemon ability (Optional)', max_length=100, required=False)
    item = forms.CharField(label='Your Pokemon\'s item (Optional)', max_length=100, required=False)
    opp_current_HP = forms.IntegerField(label='Opponent\'s  Pokemon current HP (Optional)', required=False)
    opp_num_pokemon = forms.IntegerField(label='How many pokemon left on opponent team (including this one) (Optional)', required=False)
    #TODO incorporate opponent information if user enters manually
    # opp_level = forms.IntegerField(label='Opponent\'s Pokemon level (Optional)', required=False)
    # opp_nature = forms.ChoiceField(choices=nature_choices, label='Opponent\'s  Pokemon nature (Optional)')
    # opp_item = forms.CharField(label='Opponent\'s Pokemon\'s item (Optional)', max_length=100, required=False)
    # opp_ability = forms.CharField(label='Opponent\'s  Pokemon ability (Optional)', max_length=100, required=False)
    # opp_move1 = forms.CharField(label='Opponent\'s  Pokemon move 1 (Optional)', max_length=100, required=False)
    # opp_move2 = forms.CharField(label='Opponent\'s  Pokemon move 2 (Optional)', max_length=100, required=False)
    # opp_move3 = forms.CharField(label='Opponent\'s  Pokemon move 3 (Optional)', max_length=100, required=False)
    # opp_move4 = forms.CharField(label='Opponent\'s  Pokemon move 4 (Optional)', max_length=100, required=False)
    # opp_move1_type = forms.ChoiceField(choices=type_choices, label='Opponent Pokemon move 1 type')
    # opp_move1_category = forms.ChoiceField(choices=category_choices, label='Opponent Pokemon move 1 category')
    # opp_move2_type = forms.ChoiceField(choices=type_choices, label='Opponent Pokemon move 2 type')
    # opp_move2_category = forms.ChoiceField(choices=category_choices, label='Opponent Pokemon move 2 category')
    # opp_move3_type = forms.ChoiceField(choices=type_choices, label='Opponent Pokemon move 3 type')
    # opp_move3_category = forms.ChoiceField(choices=category_choices, label='Opponent Pokemon move 3 category')
    # opp_move4_type = forms.ChoiceField(choices=type_choices, label='Opponent Pokemon move 4 type')
    # opp_move4_category = forms.ChoiceField(choices=category_choices, label='Opponent Pokemon move 4 category')