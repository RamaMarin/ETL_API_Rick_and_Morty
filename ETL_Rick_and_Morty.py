import requests  # Importa la biblioteca 'requests' para hacer peticiones HTTP (descargar datos de la web).
import json  # Importa la biblioteca 'json' para trabajar con datos en formato JSON.
import pymongo  # Importa la biblioteca 'pymongo', el driver de Python para MongoDB.
import time  # Importa la biblioteca 'time' para usar funciones relacionadas con el tiempo (como sleep).


def extraction_api(url):  # Define una función llamada 'extraction_api' que toma una 'url' como argumento.

    url_api = requests.get(url)  # Realiza una petición GET a la URL proporcionada y guarda la respuesta en 'url_api'.
    
    try:  # Inicia un bloque 'try' para manejar posibles errores durante la ejecución del código.
        
        if url_api.status_code == 200:  # Comprueba si el código de estado de la respuesta HTTP es 200 (OK).
            
            data = url_api.json()  # Si la respuesta es exitosa, convierte el contenido JSON a un diccionario de Python.
            return data  # Devuelve el diccionario con los datos.
        else:  # Si el código de estado no es 200 (por ejemplo, 404, 500, etc.).
            return {  # Devuelve un diccionario con un mensaje de error y el código de estado de la respuesta.
                'Message': 'Error in the connection',
                'Status' : url_api.status_code  # Nota: Se corrigió 'url.api' por 'url_api' para evitar un error.
            }
    
    except Exception as e:  # Captura cualquier otro tipo de error que pueda ocurrir en el bloque 'try'.
        return e  # Devuelve el objeto de excepción que contiene la información del error.


def transformation_api(data):  # Define una función llamada 'transformation_api' que toma un diccionario 'data' como argumento.
    
    personajes_originales = data.get('results', [])  # Extrae el valor asociado a la clave 'results' del diccionario 'data'. Si la clave no existe, devuelve una lista vacía.
    
    personajes_transformados = []  # Crea una lista vacía que se usará para almacenar los diccionarios de personajes transformados.

    for personajes in personajes_originales:  # Inicia un bucle 'for' para iterar sobre cada diccionario (personaje) en la lista 'personajes_originales'.
        
        if personajes.get('status') == 'Alive' and personajes.get('species') == 'Human':  # Comprueba si el estado del personaje es "Alive" y su especie es "Human".
            
            id = personajes.get('id')  # Extrae el valor del 'id' del personaje de forma segura.
            name = personajes.get('name')  # Extrae el valor del 'name' del personaje de forma segura.
            status = personajes.get('status')  # Extrae el valor del 'status' del personaje de forma segura.
            species = personajes.get('species')  # Extrae el valor del 'species' del personaje de forma segura.
            gender = personajes.get('gender')  # Extrae el valor del 'gender' del personaje de forma segura.
            origin_name = personajes.get('origin', {}).get('name', 'Desconocido')  # Extrae el nombre del origen de forma segura.
            location_name = personajes.get('location', {}).get('name', 'Desconocido')  # Extrae el nombre de la ubicación de forma segura.
            
            personaje_limpio = {  # Crea un nuevo diccionario con las claves renombradas y los valores extraídos.
                "ID_personaje": id,
                "Nombre_Personaje": name,
                "Estado de vida": status,
                "Especie": species,
                "Genero": gender,
                "Origen": origin_name,
                "Ubicacion_Actual": location_name
            }
            
            personajes_transformados.append(personaje_limpio)  # Añade el nuevo diccionario a la lista de personajes transformados.

    return personajes_transformados  # Devuelve la lista completa de diccionarios transformados.


def loading_api(personajes_transformados):  # Define una función para la fase de carga.
    
    client = pymongo.MongoClient("localhost:27017")  # Crea una conexión con el cliente de MongoDB.
    db = client['rick_and_morty']  # Accede a la base de datos 'rick_and_morty' o la crea si no existe.
    collection = db['personajes_limpios']  # Accede a la colección 'personajes_limpios' o la crea si no existe.
    
    collection.insert_many(personajes_transformados)  # Inserta todos los diccionarios de la lista en la colección.
    
    
if __name__ == "__main__":  # Este bloque de código solo se ejecuta si el script se corre directamente.
    time.sleep(5)  # Pausa la ejecución del script por 5 segundos.
    
    print("\nStarting ETL process")  # Imprime un mensaje indicando el inicio del proceso.
    
    print("\nExtracting data...")  # Imprime un mensaje para la fase de extracción.
    data = extraction_api("https://rickandmortyapi.com/api/character")  # Llama a la función 'extraction_api' y guarda el resultado.
    
    print("\nTransforming data...")  # Imprime un mensaje para la fase de transformación.
    personajes_transformados = transformation_api(data)  # Llama a la función 'transformation_api' con los datos extraídos.
    
    print("\nLoading into the MongoDB...")  # Imprime un mensaje para la fase de carga.
    loading_api(personajes_transformados)  # Llama a la función 'loading_api' para insertar los datos en MongoDB.
    
    for personaje in personajes_transformados:  # Itera sobre cada diccionario (personaje) en la lista 'personajes_transformados'.
        
        for key, value in personaje.items():  # Itera sobre cada par clave-valor del diccionario actual.
            print(f" - {key}: {value}")  # Imprime cada par clave-valor con un formato limpio.
                
        print("-------------")  # Imprime una línea separadora entre los registros de los personajes.