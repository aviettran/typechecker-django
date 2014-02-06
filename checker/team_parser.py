from pokedex.db import connect, tables, util
import re

def getName(name):
    return name.partition(' ')[0].strip()

def getPokemonList(s):
    session = connect()
#    f = open(filename,'r')
    f = s.splitlines(True)
    print f
    pokemon_list = []
    next_pokemon = True
    for line in f:
        if next_pokemon and line != '\r\n':
            pokemon_list.append(getName(line))
            next_pokemon = False
        elif line == '\r\n':
            next_pokemon = True
    return pokemon_list

