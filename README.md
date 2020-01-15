# InkBrutalMarketing

# Instalar python 3.7 o sup

# Lista de comandos usados hasta el momento

# Para instalar django
pip install django

# Para instalar DjangoRestFramework
pip install djangorestframework

# Para crear proyecto en Django
django-admin startproject "nombre del proyecto"

# Para crear las distintas aplicaciones del proyecto
django-admin startapp "nombre de la aplicación"

# Para ejecutar el servidor
python manage.py runserver

# Para descargar el driver y poder conectarnos con MySql
pip install mysqlclient

# Para crear las migraciones
python manage.py makemigrations   <- Ejecuta todas las migraciones
python manage.py makemigrations "nombre de la aplicación"   <- Ejecuta la migración de solo "nombre de la aplicación"

# Para efectuar los cambios en la BD
python manage.py migrate

# Para crear un super usuario en la BD
python manage.py createsuperuser

# Para instalar las dependencias necesarias en el proyecto
pip install django-rest-auth
pip install django-allauth
pip install django-registration
pip install django-crispy-forms

# Para que se pueda comunicar Django REST con Vue
pip install django-webpack-loader

# Para guardar las dependencias (en un txt) necesarias para el proyecto
pip freeze > requirements.txt

# Para descargar las dependencias actuales del proyecto
pip install -r requirements.txt

# Instalación de VueJs
npm install @vue/cli

# Creación de un proyecto en VueJs
vue create "nombre"
    ->manually
    ->(Babel - Router - Linter/Formatter)
    ->Yes
    ->Prettier
    ->Lint on save
    ->in package.json
    ->No

# Ejecutar el siguiente comando para instalar una dependencia en el entorno de desarrollo
vue ui
    Instalar laa dependencia webpack-bundle-tracker

# Correr el proyecto VueJs
npm run serve