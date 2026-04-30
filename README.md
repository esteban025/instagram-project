# INSTAGRAM (SOCIAL NETWORK) - PROJECT DJANGO

### Objectivo del proyecto

Poner en practica todo lo aprendido dentro del curso de Django, creacion de modelos, y vistas similares a la aplicacion, una aplicacion similar a la plataforma de Instagram.

---

## FASE 1 - Inicializacion y configuracion del proyecto

1. Creacion del proyecto
  - [✔] Creacion de README e inicializar con git.
  - [✔] Creacion del entorno virtual. **py -m venv venv**
  - [✔] Activar el entorno virtual. **venv\Scripts\activate**
  - [✔] Instalacion de Django. **pip install django**
  - [✔] Creacion del proyecto. **django-admin startproject config .**
  - [✔] Creacion de la aplicacion. **python manage.py startapp instagram**
  - [✔] Creamos los requerimeintos de este proyecto **pip freeze > requirements.txt**
  - [✔] Creacion de la base de datos. **python manage.py migrate**
  - [✔] Creacion del superusuario. **python manage.py createsuperuser**
- [✔] Inicializacion del servidor. **python manage.py runserver**

2. Configuracion del proyecto
  - [✔] Configuracion de la aplicacion en settings.py
  - [✔] Configuracion de la base de datos
  - [✔] Configuracion del superusuario
  - [✔] Configuracion del servidor
  - [ ] Instalacion de extensiones adicionales **pip install django-extensions**

3. Creacion de apps 
  - [✔] Creacion de profiles, posts, notifications, etc.
  - [✔] Configuracion de las apps en settings.py

---

## Fase 2 - Creacion de modelos

1. Creacion de modelos
  - [✔] Creacion de modelos para profiles, posts.
  - [✔] Configuracion de los modelos en settings.py
  - [✔] Creacion de las migraciones **python manage.py makemigrations**
  - [✔] Aplicacion de las migraciones **python manage.py migrate**

---

## Fase 3 - Creacion de vistas
1. Creacion de vistas
  - [✔] Creacion de vista general de la aplicacion, sin funcionamiento
  - [✔] Vista de header y posts

## Fase 4 - Registro de usuarios y login

1. Registros.
  - [✔] Creacion de vista de registro
  - [✔] Creacion de vista de login
  - [✔] Creacion de vista de logout

2. Configuraciones
  - [✔] Configuracion de las vistas en urls.py
  - [✔] Configuracion de las vistas en settings.py

3. Correciones
  - [✔] Cada vez que registramos un usuario, creamos un perfil con la misma informacion.
  - [✔] Rectificamos el disenio de fotos de perfil y demas.
  
---

## Fase 5

1. Creacion y edicion de perfil por el usuario
  - [ ] Creamos la vista de editar perfil.