# challenge-claroshop
## Author: Luis Fidel Escobar Ambrosio

## Resume

Esta es una API rest creada con Flask

La API debe tener las siguientes rutas:

- GET /pokemons: Lista todos los Pokémon.
- GET /pokemon/<int:id>: Obtiene detalles de un Pokémon específico por su ID.

La API base es `localhost:5000/`

## Requirementos

- Tener instalado Python (3.12.5)
- Tener instalado virtualenv
  

1. Abrir el proyecto con el IDE de su preferencia
2. Instala el entorno virtual en el directorio del proyecto con `pip install virtualenv`
3. Crea un entorno virtual en el directorio del proyecto con `python -m venv venv`
4. Activa el entorno virtual `.\venv\Scripts\activate.ps1` en windows y ejecuta 
`pip install -r requirements.txt`
5. Ejecuta con  `flask run`
6. Ejecuta las pruebas con   `pytest`

## Respositorio en Github

`git clone https://github.com/FideruEscobar/challenge_claroshop.git`

## Nota:

Si no se tiene el .env favor de crearlo y poner esta variable

API_URL = "https://pokeapi.co/api/v2/"



