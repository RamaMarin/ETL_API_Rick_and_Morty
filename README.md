# Proyecto ETL de Rick y Morty

## Descripción del Proyecto

Este proyecto es un pipeline de **ETL (Extract, Transform, Load)** desarrollado en Python que procesa datos de la famosa serie animada "Rick y Morty". 
El objetivo principal es extraer información de personajes de la API pública de Rick y Morty, aplicar transformaciones específicas para filtrar y limpiar los datos, y finalmente 
cargar los resultados en una base de datos **MongoDB**.

**El objetivo de la transformación es: filtrar solo los personajes que están "Alive" (Vivos) y son de la especie "Human" (Humana), y luego estructurar los campos de manera más limpia.**

Este proyecto demuestra habilidades en:
* Consumo de APIs RESTful.
* Manipulación y limpieza de datos con Python.
* Persistencia de datos en bases de datos NoSQL (MongoDB).
* Desarrollo de pipelines de datos simples.

## Tecnologías Utilizadas

* **Python 3.x**
* **`requests`**: Para realizar peticiones HTTP a la API.
* **`json`**: Para trabajar con datos en formato JSON.
* **`pymongo`**: Driver de Python para interactuar con MongoDB.
* **MongoDB**: Base de datos NoSQL para el almacenamiento final de los datos transformados.

## Estructura del Repositorio

* `ETL_Rick_and_Morty.py`: Script principal que contiene las funciones de Extracción, Transformación y Carga.
* `requirements.txt`: Archivo que lista todas las dependencias de Python necesarias para ejecutar el proyecto.
* `data/`:
    * `rick_and_morty.personajes_limpios.json`: Un archivo JSON de ejemplo que muestra los datos tal como son cargados en MongoDB después de la transformación.

## Configuración y Ejecución

Para ejecutar este proyecto localmente, sigue los siguientes pasos:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/TuUsuario/ETL_Rick_and_Morty.git](https://github.com/TuUsuario/ETL_Rick_and_Morty.git)
    cd ETL_Rick_and_Morty
    ```
2.  **Configurar un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    # En Windows
    .\venv\Scripts\activate
    # En macOS/Linux
    source venv/bin/activate
    ```
3.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Instalar y configurar MongoDB:**
    Asegúrate de tener una instancia de MongoDB corriendo localmente en el puerto `27017`. Puedes descargar MongoDB Community Edition desde su [sitio web oficial](https://www.mongodb.com/try/download/community).
    
    > **Nota para MongoDB:** El script asume que MongoDB está corriendo en `localhost:27017`. Si tu configuración es diferente, deberás modificar la línea de conexión en `ETL_Rick_and_Morty.py`: `client = pymongo.MongoClient("localhost:27017")`.

5.  **Ejecutar el script ETL:**
    ```bash
    python ETL_Rick_and_Morty.py
    ```
    El script imprimirá el estado del proceso en la consola y, al finalizar, los personajes transformados que se insertaron en la base de datos `rick_and_morty` en la colección `personajes_limpios`.

## Datos Transformados de Ejemplo

El archivo `data/rick_and_morty.personajes_limpios.json` contiene un extracto de los datos resultantes después de la transformación y carga en MongoDB. Cada documento representa un personaje "Humano" y "Vivo" con los campos seleccionados y renombrados.

Aquí un ejemplo de un registro:
```json
{
  "ID_personaje": 1,
  "Nombre_Personaje": "Rick Sanchez",
  "Estado de vida": "Alive",
  "Especie": "Human",
  "Genero": "Male",
  "Origen": "Earth (C-137)",
  "Ubicacion_Actual": "Citadel of Ricks"
}
