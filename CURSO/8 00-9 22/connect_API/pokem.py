#
#https://pokeapi.co/
#
import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_data(name):
    url = f"{base_url}/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    print(response)
    
    #response.status_code nos tira el codigo de si lo encontro o no, podria arrojar el error 404
    if response.status_code == 200:
        pokemon_data = response.json() #lo convierte en un diccionario
        return pokemon_data
    else:
        print(f"No se pudo acceder al dato {response.status_code}")

pokemon_name = "gyarados"
poke_info = get_pokemon_data(pokemon_name)

if poke_info:
    print(f"Name: {poke_info["name"]}")
    print(f"ID: {poke_info["id"]}")
    print(f"Height: {poke_info["height"]}")
    print(f"Weight: {poke_info["weight"]}")