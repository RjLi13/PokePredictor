from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from poke_set_info import set_bw, set_dpp, set_gsc, set_rby, set_rse

# Create your views here.
def index(request):
    return render(request, 'predictor/index.html')

def search(request):
    try:
        search_id = request.POST['mytextbox']
    except KeyError:
        print("Pokemon not found")
        return render(request, 'predictor/index.html')
    return HttpResponseRedirect(reverse('predictor:results', args=(search_id,)))

def results(request, search_id):
    poke1_sets = set_bw[search_id]
    # return HttpResponse("You're looking at %s." % poke1_sets)
    return render(request, 'predictor/results.html', {'poke1_sets': poke1_sets})