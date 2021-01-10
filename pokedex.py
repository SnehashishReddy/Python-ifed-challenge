import PySimpleGUI as sg
import requests

def type_find(pokemon_name):
    type_list = []
    pokeAPI_general_url = 'https://pokeapi.co/api/v2/pokemon/'
    pokemon_url = pokeAPI_general_url + pokemon_name
    try:
        response = requests.get(pokemon_url)
        data = (response.json())['types']
        for x in data:
            type_list.append(x['type']['name'])
        return type_list
    except ValueError:
        return 0

def double_damage_from(pokemon_name):
    double_damage_list = []
    pokeAPI_general_url = 'https://pokeapi.co/api/v2/pokemon/'
    pokemon_url = pokeAPI_general_url + pokemon_name
    try:
        response = requests.get(pokemon_url)
        data = (response.json())['types']
        for a in range(0,len(data)):
            x = data[a]
            new_url = x['type']['url']
            try:
                type_poke = []
                new_response = requests.get(new_url)
                new_data = (new_response.json())['damage_relations']['double_damage_from']
                for y in new_data:
                	type_poke.append(y['name'])
                double_damage_list.append(type_poke)
            except ValueError:
                return 0
        return double_damage_list
    except ValueError:
        return 0
    
def double_damage_from_list(pokemon_name):
    final_list = []
    pokeAPI_general_url = 'https://pokeapi.co/api/v2/pokemon/'
    pokemon_url = pokeAPI_general_url + pokemon_name
    try:
        response = requests.get(pokemon_url)
        data = (response.json())['types']
        for x in data:
            new_url = x['type']['url']
            try:
                new_response = requests.get(new_url)
                new_data = (new_response.json())['damage_relations']['double_damage_from']
                for y in new_data:
                    brand_new_url = y['url']
                    try:
                        double_damage_poke_list = []
                        brand_new_response = requests.get(brand_new_url)
                        brand_new_data = (brand_new_response.json())['pokemon']
                        for z in range(0,5):
                            double_damage_poke_list.append(brand_new_data[z]['pokemon']['name'])
                        final_list.append(double_damage_poke_list)
                    except ValueError:
                        return 0
            except ValueError:
                return 0
        return final_list
    except ValueError:
        return 0

def ability(pokemon_name):
    ability_list = []
    pokeAPI_general_url = 'https://pokeapi.co/api/v2/pokemon/'
    pokemon_url = pokeAPI_general_url + pokemon_name
    try:
        response = requests.get(pokemon_url)
        data = (response.json())['abilities']
        for x in data:
            ability_list.append(x['ability']['name'])
        return ability_list
    except ValueError:
        return 0

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Pokedex')],
          [sg.Text('Please enter the name of the pokemon: '),
           sg.InputText(key='ab0')],
          [sg.Button('Retrieve Details'), sg.Button('Close')]]

# Create the Window
window = sg.Window('Window Title', layout, element_justification='c')
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    if event == 'Retrieve Details':
        type_list = type_find(values['ab0'])
        double_damage_from_simple_list = double_damage_from(values['ab0'])
        double_damage_from_larger_list = double_damage_from_list(values['ab0'])
        ability_list = ability(values['ab0'])
        sg.Print(values['ab0'].upper())
        sg.Print('')
        sg.Print('The types that the pokemon {} holds are: '.format(values['ab0']))
        for x in type_list:
            sg.Print(x)
        sg.Print('')
        sg.Print('The types of pokemon that can cause double damage to {} are: '.format(values['ab0']))
        for x in double_damage_from_simple_list:
            for y in x:
                sg.Print(y)
        sg.Print('')
        sg.Print('Some of the pokemons that can cause double damage to {} are: '.format(values['ab0']))
        sg.Print('')
        identifier = 0
        for x in double_damage_from_simple_list:
            for y in x:
                sg.Print('{} type pokemon: '.format(y))
                for z in double_damage_from_larger_list[identifier]:
                    sg.Print(z)
                sg.Print('')
            identifier+=1
        sg.Print('The ablities of {} are: '.format(values['ab0']))
        for x in ability_list:
            sg.Print(x)
window.close()