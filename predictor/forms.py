__author__ = 'ruijing'
from django import forms

class PokeForm(forms.Form):
    name = forms.CharField(label='Your Pokemon name', max_length=30)
    level = forms.IntegerField(label='Your Pokemon level')
    current_HP = forms.IntegerField(label='Your Pokemon current HP')
    nature = forms.CharField(label=' Your Pokemon nature', max_length=50)
    ability = forms.CharField(label='Your Pokemon ability', max_length=100)
    move1 = forms.CharField(label='Your Pokemon move 1', max_length=100)
    move2 = forms.CharField(label='Your Pokemon move 2', max_length=100)
    move3 = forms.CharField(label='Your Pokemon move 3', max_length=100)
    move4 = forms.CharField(label='Your Pokemon move 4', max_length=100)
    opp_name = forms.CharField(label='Opponent\'s Pokemon name', max_length=30)
    opp_level = forms.IntegerField(label='Opponent\'s Pokemon level')
    opp_current_HP = forms.IntegerField(label='Opponent\'s  Pokemon current HP')
    opp_nature = forms.CharField(label='Opponent\'s  Pokemon nature', max_length=50)
    opp_ability = forms.CharField(label='Opponent\'s  Pokemon ability', max_length=100)
    opp_move1 = forms.CharField(label='Opponent\'s  Pokemon move 1', max_length=100)
    opp_move2 = forms.CharField(label='Opponent\'s  Pokemon move 2', max_length=100)
    opp_move3 = forms.CharField(label='Opponent\'s  Pokemon move 3', max_length=100)
    opp_move4 = forms.CharField(label='Opponent\'s  Pokemon move 4', max_length=100)