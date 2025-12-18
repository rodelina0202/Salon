# Proyecto Salón

## Descripción
Este proyecto es una aplicación en Python que permite realizar operaciones CRUD
(Crear, Leer, Actualizar y Eliminar) utilizando una base de datos en Supabase.
Está diseñado como práctica académica para la asignatura "Big Data".

## Estructura del proyecto
- conexion.py: Maneja la conexión con la base de datos Supabase.
- funciones.py: Contiene las funciones CRUD del sistema.
- utilidades.py: Funciones auxiliares como mensajes, validaciones y utilidades.
- main.py: Archivo principal que ejecuta el programa.

## Tecnologías utilizadas
- Python
- Supabase
- python-dotenv

## Configuración
Antes de ejecutar el proyecto, se debe crear un archivo `.env` con las siguientes variables:

SUPABASE_URL=tu_url_de_supabase  
SUPABASE_KEY=tu_key_de_supabase  
TABLA1=nombre_tabla  
TABLA2=nombre_tabla  
TABLA3=nombre_tabla  
TABLA4=nombre_tabla  
supabase = create_client(url,key)

## Ejecución
Para ejecutar el proyecto, correr el siguiente comando:

python main.py

## Autora
Rodelina De La Rosa Sarante.