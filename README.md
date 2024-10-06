# PROYECTO VEHÍCULOS
Práctica de consolidación M6

## Descripción
Proyecto creado en el entorno de desarrollo python/django, para gestionar información sobre autos a nivel usuario y administrativo

## Requisitos
- Python 3.x
- IDE de su preferencia
- Navegador web

### Configuración probada
- Python 3.12.1
- Visual Studio Code
- Microsoft Edge

## Instalación y configuración (dev)
1) Clonar el repositorio
    ```bash
    git clone https://github.com/AllanMoralesPrado/proyecto-vehiculos-django.git
    ```
2) Crear, activar y configurar un entorno virtual
    venv
    ```bash
    cd proyecto-vehiculos-django
    py -m venv vehiculos-django-env
    ./vehiculos-django-env/Scripts/activate
    ```
    virtualenvwrapper
    ```bash
    cd proyecto-vehiculos-django
    mkvirtualenv vehiculos-django-env
    workon vehiculos-django-env
    ```
3) Instalar dependencias
    ```bash
    py -m pip install -r requirements.txt
    ```
4) Crear archivo .env con los siguientes pares clave-valor:
    ```dotenv
    SECRET_KEY='tu_clave_secreta'
    DEBUG=False
    ```
5) Aplicar las migraciones
    ```bash
    py manage.py migrate
    ```
6) Levantar el servidor
    ```bash
    py manage.py runserver
    ```