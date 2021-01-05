from django.shortcuts import render
from .models import Parasite

# Create your views here.

def more_parasites(request):
    return render(request, 'more_parasites.html')


def default_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'

    return render(request, 'default.html',{ 'mapbox_access_token': mapbox_access_token })

def plasmodium_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    parasite = Parasite.objects.get(name='Plasmodium')

    return render(request, 'plasmodium.html', { 'mapbox_access_token': mapbox_access_token, 'parasite': parasite })

def leishmania_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    parasite = Parasite.objects.get(name='Leishmania')

    return render(request, 'leishmania.html',{ 'mapbox_access_token': mapbox_access_token, 'parasite': parasite })

def trypanosoma_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    parasite = Parasite.objects.get(name='Trypanosoma')

    return render(request, 'trypanosoma.html',{ 'mapbox_access_token': mapbox_access_token, 'parasite': parasite })

def ascaris_lumbricoides_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    parasite = Parasite.objects.get(name='Ascaris Lumbricoides')

    return render(request, 'ascaris.html',{ 'mapbox_access_token': mapbox_access_token, 'parasite': parasite })

def trichinella_spiralis_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    parasite = Parasite.objects.get(name='Trichinella Spiralis')

    return render(request, 'trichinella.html',{ 'mapbox_access_token': mapbox_access_token, 'parasite': parasite })