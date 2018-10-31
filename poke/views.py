from django.shortcuts import render
from poke.models import Pokeyman

# Create your views here.

def poke_view(request):
    poke = Pokeyman.objects.all() # pylint: disable=E1101
    return render(request, 'poke/pokelist.html', {
        'pokelist': poke,
    })
