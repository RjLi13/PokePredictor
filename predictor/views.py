from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .forms import PokeForm

from utils import *

# Create your views here.
def index(request):
    return render(request, 'predictor/index.html')

def search(request):
    try:
        search_id = request.POST['mytextbox']
    except KeyError:
        print("Pokemon not found")
        return render(request, 'predictor/index.html')
    custom = 1
    return HttpResponseRedirect(reverse('predictor:results', args=(search_id,custom,)))

def query(request):
    if request.method == 'POST':
        form = PokeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            lvl = form.cleaned_data['level']
            cHP = form.cleaned_data['current_HP']
            nature = form.cleaned_data['nature']
            ability = form.cleaned_data['ability']
            move1 = form.cleaned_data['move1']
            move2 = form.cleaned_data['move2']
            move3 = form.cleaned_data['move3']
            move4 = form.cleaned_data['move4']
            opp_name = form.cleaned_data['opp_name']
            opp_lvl = form.cleaned_data['opp_level']
            opp_cHP = form.cleaned_data['opp_current_HP']
            opp_nature = form.cleaned_data['opp_nature']
            opp_ability = form.cleaned_data['opp_ability']
            move = choose_move(name,lvl, cHP, nature, ability, opp_name, opp_lvl, opp_cHP, opp_nature, opp_ability, move1, move2, move3, move4)
            return HttpResponse(move)
    else:
        form = PokeForm()
    return render(request, 'predictor/pokeform.html', {'form': form})


def results(request, search_id, custom):
    search_id = str(search_id)
    search_id = search_id.lower()
    if custom == '1':
        upper_char = search_id[0].upper()
        print upper_char
        search_id = upper_char + search_id[1:]
        poke1_sets = set_bw[search_id]
        return render(request, 'predictor/results.html', {'poke1_sets': poke1_sets, 'custom': True})
