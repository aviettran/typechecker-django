# Create your views here.
from django.shortcuts import render
from team_parser import getPokemonList
from pokedex.db import connect, tables, util

def results(request):

    session = connect()

    try:
        team_text = request.POST['text']
    except:
        team_text = 'No team loaded'

    #Get the array of party Pokemon as strings
    pokemon_list = getPokemonList(team_text)

    #Get party_list, an array of tables.Pokemon
    party_list = []
    pokemon_type_list = []
    for i in range(0,len(pokemon_list)):
        try:
            party_list.append(util.get(session, tables.PokemonSpecies, name=pokemon_list[i]).default_pokemon)
            continue
        except:
            pass
        try:
            party_list.append(util.get(session, tables.Pokemon, pokemon_list[i].lower()))
        except:
            pass

    #The max resist for a certain type
    max_resists = []

    #Get list of types as tables.Type
    type_query = session.query(tables.Type)

    for (i, type) in enumerate(type_query):
        if i > 17:
            break
        max_resists.append([type.name, 100])
        for pokemon in party_list:
            resist = 1
            for type in pokemon.types:
                resist = resist * type.target_efficacies[i].damage_factor / 100.0
            if resist < max_resists[i][1]:
                max_resists[i][1] = resist

    return render(request, 'checker/results.html', {'party_list': party_list, 'max_resists': max_resists, 'team_text': team_text})

def index(request):
    return render(request, 'checker/index.html')
