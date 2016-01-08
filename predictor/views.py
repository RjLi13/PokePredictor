from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .forms import PokeForm

from utils import *

# Create your views here.
def index(request):
    return render(request, 'predictor/index.html')

def query(request):
    if request.method == 'POST':
        form = PokeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            lvl = form.cleaned_data['level']
            cHP = form.cleaned_data['current_HP']
            nature = form.cleaned_data['nature']
            ability = form.cleaned_data['ability']
            item = form.cleaned_data['item']
            move1 = form.cleaned_data['move1']
            move1_type = form.cleaned_data['move1_type']
            move2_type = form.cleaned_data['move2_type']
            move3_type = form.cleaned_data['move3_type']
            move4_type = form.cleaned_data['move4_type']
            move1_category = form.cleaned_data['move1_category']
            move2_category = form.cleaned_data['move2_category']
            move3_category = form.cleaned_data['move3_category']
            move4_category = form.cleaned_data['move4_category']
            move2 = form.cleaned_data['move2']
            move3 = form.cleaned_data['move3']
            move4 = form.cleaned_data['move4']
            evs = {}
            ev_hp = form.cleaned_data['ev_hp']
            if ev_hp is not None:
                evs['hp'] = ev_hp
            ev_atk = form.cleaned_data['ev_atk']
            if ev_atk is not None:
                evs['at'] = ev_atk
            ev_def = form.cleaned_data['ev_def']
            if ev_def is not None:
                evs['df'] = ev_def
            ev_spatk = form.cleaned_data['ev_spatk']
            if ev_spatk is not None:
                evs['sa'] = ev_spatk
            ev_spdef = form.cleaned_data['ev_spdef']
            if ev_spdef is not None:
                evs['sd'] = ev_spdef
            ev_speed = form.cleaned_data['ev_speed']
            if ev_speed is not None:
                evs['sp'] = ev_speed
            opp_name = form.cleaned_data['opp_name']
            opp_cHP = form.cleaned_data['opp_current_HP']
            num_pokemon = form.cleaned_data['num_pokemon']
            opp_num_pokemon = form.cleaned_data['opp_num_pokemon']
            # TODO incorporate opponent info into this
            #opp_lvl = form.cleaned_data['opp_level']
            # opp_nature = form.cleaned_data['opp_nature']
            # opp_ability = form.cleaned_data['opp_ability']
            # opp_move1 = form.cleaned_data['opp_move1']
            # opp_move2 = form.cleaned_data['opp_move2']
            # opp_move3 = form.cleaned_data['opp_move3']
            # opp_move4 = form.cleaned_data['opp_move4']
            # opp_move1_type = form.cleaned_data['opp_move1_type']
            # opp_move2_type = form.cleaned_data['opp_move2_type']
            # opp_move3_type = form.cleaned_data['opp_move3_type']
            # opp_move4_type = form.cleaned_data['opp_move4_type']
            # opp_move1_category = form.cleaned_data['opp_move1_category']
            # opp_move2_category = form.cleaned_data['opp_move2_category']
            # opp_move3_category = form.cleaned_data['opp_move3_category']
            # opp_move4_category = form.cleaned_data['opp_move4_category']
            # opp_move2 = form.cleaned_data['move2']
            # opp_move3 = form.cleaned_data['move3']
            # opp_move4 = form.cleaned_data['move4']
            # opp_item = form.cleaned_data['item']

            move = choose_move(name,lvl, cHP, nature, ability, opp_name, opp_cHP,
                               move1, move2, move3, move4, move1_type, move2_type, move3_type, move4_type, move1_category,
                               move2_category, move3_category, move4_category, item, num_pokemon, opp_num_pokemon, evs)
            return HttpResponse(move)
    else:
        form = PokeForm()
    return render(request, 'predictor/pokeform.html', {'form': form})

