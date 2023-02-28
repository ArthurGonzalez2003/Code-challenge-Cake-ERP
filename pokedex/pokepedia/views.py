from django.shortcuts import render
import requests

# PokéApi Data Fetching/Scrapying.

def get_name(pkm):
    pkm_name = pkm['forms'][0]['name']
    return(pkm_name)

def get_profile(pkm, hdimg):
    if hdimg:
        picture_link = pkm['sprites']['other']['dream_world']['front_default']
        return(picture_link)
    else:
        picture_link = pkm['sprites']['front_default']
        return(picture_link)

def get_abilities(pkm):
    abilities = []
    for i in pkm['abilities']:
        abilities.append(i['ability']['name'])
    return(abilities)

def get_types(pkm):
    types = []
    for i in pkm['types']:
        types.append(i['type']['name'])
    return(types)

def fetch_data(pkm, hdimg):
    api = ("https://pokeapi.co/api/v2/pokemon/"+ pkm)
    res = requests.get(api)
    pkm = res.json()
    data = {"name": get_name(pkm),
            "imglink": get_profile(pkm, hdimg),
            "abilities" : get_abilities(pkm),
            "types": get_types(pkm)
            }
    return data
    
# Create your views here.

def index(request):
    return render(request, "pokepedia/index.html")

def pokemon_data(request, pkm):
    data = fetch_data(pkm, hdimg=False)
    return render(request, "pokepedia/pokemon-data.html", {'data':data})

def pokemon_data_hd(request, pkm):
    data = fetch_data(pkm, hdimg=True)
    return render(request, "pokepedia/pokemon-data.html", {'data':data})
