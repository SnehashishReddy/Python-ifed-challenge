def ability(pokemon_name):
    '''Summary of the ability function
    
    Parameters:
    pokemon_name (string): Pass the name of the pokemon whose abilites we want to obtain to the function
    
    Returns:
    ability_list (list): The returned object will be a list which contains all the abilities of said pokemon.
    
    Note: If the given pokemon name cannot be found, 0 will be returned instead
    
    '''
    # Importing the requests library for use
    import requests
    
    ability_list = []
    pokeAPI_general_url = 'https://pokeapi.co/api/v2/pokemon/'
    pokemon_url = pokeAPI_general_url + pokemon_name # This step will prepare the url we need for the API request
    try: # This step is to check if the pokemon name entered is right or wrong.
        response = requests.get(pokemon_url) # An API request is being made to the url
        data = (response.json())['abilities'] # The obtained json info is being converted into a python dictionary. From that the abilities key is being chosen
        for x in data:
            ability_list.append(x['ability']['name']) # Every ability has a unique ability attribute and a name, so that info is being extracted
        return ability_list
    except ValueError: # This will be the error returned if the given pokemon name is incorrect
        return 0