import requests
import json
import os

# Función para obtener los datos del Pokémon
def obtener_pokemon(nombre):
    # URL de la PokéAPI
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    
    try:
        # Hacemos la petición a la API
        response = requests.get(url)
        
        # Si la respuesta es exitosa (código 200)
        if response.status_code == 200:
            # Parseamos la respuesta JSON
            data = response.json()

            # Extraemos la información del Pokémon
            pokemon_data = {
                'nombre': data['name'],
                'peso': data['weight'],
                'tamaño': data['height'],
                'tipos': [tipo['type']['name'] for tipo in data['types']],
                'habilidades': [habilidad['ability']['name'] for habilidad in data['abilities']],
                'movimientos': [movimiento['move']['name'] for movimiento in data['moves']],
                'imagen': data['sprites']['front_default']
            }

            # Mostrar la imagen y la información en consola
            print(f"Nombre: {pokemon_data['nombre']}")
            print(f"Peso: {pokemon_data['peso']}")
            print(f"Tamaño: {pokemon_data['tamaño']}")
            print(f"Tipos: {', '.join(pokemon_data['tipos'])}")
            print(f"Habilidades: {', '.join(pokemon_data['habilidades'])}")
            print(f"Movimientos: {', '.join(pokemon_data['movimientos'][:5])}...")  # Mostramos los primeros 5 movimientos
            print(f"Imagen: {pokemon_data['imagen']}")

            # Mostramos la imagen en un navegador o en algún visor (opcional)
            # En este caso solo mostramos la URL

            # Guardar la información en un archivo JSON
            guardar_pokemon(pokemon_data)

        else:
            print(f"Error: No se encontró el Pokémon '{nombre}'.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error al hacer la solicitud: {e}")

# Función para guardar la información del Pokémon en un archivo .json
def guardar_pokemon(pokemon_data):
    # Crear la carpeta 'pokedex' si no existe
    if not os.path.exists('pokedex'):
        os.makedirs('pokedex')

    # Nombre del archivo
    archivo = f"pokedex/{pokemon_data['nombre']}.json"
    
    # Guardamos la información en el archivo
    with open(archivo, 'w') as f:
        json.dump(pokemon_data, f, indent=4)
    print(f"Información guardada en {archivo}")

# Función principal para interactuar con el usuario
def main():
    nombre_pokemon = input("Introduce el nombre del Pokémon: ")
    obtener_pokemon(nombre_pokemon)

# Ejecutar el programa
if __name__ == "__main__":
    main()