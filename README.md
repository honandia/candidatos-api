# API de Gestión de Candidatos

Este proyecto es una **API** desarrollada con **FastAPI** para gestionar candidatos. Permite recibir datos como **DNI**, **nombre** y **apellido**, y almacenarlos en una base de datos **SQLite**. 

## Requisitos

Asegúrate de tener instalados los siguientes requisitos antes de ejecutar el proyecto:

- **Python 3.7 o superior**
- **FastAPI**: Para manejar la API.
- **Uvicorn**: Para correr el servidor ASGI.
- **SQLAlchemy**: Para interactuar con la base de datos SQLite.

### Instalación de dependencias

Para instalar las dependencias, puedes ejecutar el siguiente comando:

`pip install fastapi uvicorn sqlalchemy
`
### Estructura del Proyecto

El archivo principal del proyecto es main.py. Este archivo contiene el código que define los endpoints de la API, el modelo de datos y la configuración de la base de datos.

    main.py: Contiene el código principal de la API y el modelo de base de datos.

### Base de Datos

Este proyecto utiliza SQLite para almacenar los datos de los candidatos. Cada vez que se recibe un nuevo candidato a través del endpoint, sus datos se almacenan en una tabla llamada candidatos. Los campos almacenados son:

    id: Identificador único del candidato.
    dni: Número de identificación del candidato.
    nombre: Nombre del candidato.
    apellido: Apellido del candidato.

### Endpoints
1. POST /candidato

Este endpoint permite agregar un nuevo candidato a la base de datos. Debes enviar un cuerpo de solicitud con los siguientes campos:

    dni: (String) El DNI del candidato.
    nombre: (String) El nombre del candidato.
    apellido: (String) El apellido del candidato.

**Ejemplo de solicitud
**
    POST /candidato
    {
      "dni": "12345678",
      "nombre": "Juan",
      "apellido": "Pérez"
    }

**Respuesta exitosa
**
    {
      "mensaje": "Candidato creado exitosamente",
      "candidato": {
        "id": 1,
        "dni": "12345678",
        "nombre": "Juan",
        "apellido": "Pérez"
      }
    }

**Error (DNI duplicado)
**
Si intentas crear un candidato con un DNI ya existente, recibirás una respuesta de error:

    {
      "detail": "El candidato con este DNI ya existe"
    }
    
### Ejecución del Proyecto

Para iniciar el servidor de FastAPI, usa el siguiente comando:

`uvicorn main:app --reload`

Esto iniciará el servidor en modo de recarga automática y lo expondrá en http://127.0.0.1:8000.
### Documentación de la API

FastAPI proporciona automáticamente una interfaz de usuario interactiva con la documentación de la API. Después de iniciar el servidor, puedes acceder a la documentación en:

    Swagger UI: http://127.0.0.1:8000/docs
    Redoc: http://127.0.0.1:8000/redoc

### Ejemplo de Uso

Después de iniciar el servidor, puedes enviar solicitudes POST a http://127.0.0.1:8000/candidato con un cuerpo JSON que contenga el DNI, nombre y apellido del candidato.
Ejemplo usando curl:
    
    curl -X 'POST' \
      'http://127.0.0.1:8000/candidato' \
      -H 'Content-Type: application/json' \
      -d '{
      "dni": "12345678",
      "nombre": "Juan",
      "apellido": "Pérez"
    }'

### Base de Datos SQLite

La base de datos se crea automáticamente cuando ejecutas la API. Se genera un archivo candidatos.db en el directorio raíz del proyecto.
Herramientas para explorar SQLite

Para explorar o interactuar manualmente con la base de datos SQLite, puedes utilizar herramientas como:

    DB Browser for SQLite
    La CLI de SQLite (usando el comando sqlite3 en la terminal).
