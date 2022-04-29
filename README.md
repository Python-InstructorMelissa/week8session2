# week8session2

Create Django environment (outside of any project folder)
1. python -m venv djangoEnv (or what ever you want to name it)
2. to start environment
    on mac source djangoEnv/bin/activate
    on Windows source djangoEnv/Scripts/activate
3. pip list to show packages
4. pip install --upgrade pip setuptools as required
5. pip install django bcrypt
6. pip list again should show those 4 listed above plus others
7. pip install django-environ - to use .env to hide key
8. pip install pillow - to do uploads
9. pip install ipython - for easier to read shell 

Create project
1. Enter project folder
2. django-admin startproject djangoProject . (the . keeps the root of the project in the current folder not one down)
3. python manage.py startapp djangoApp
4. python manage.py runserver (go to localhost and you should now see the rocket ship - but shut server down after or it will once you start editing)

Models
1. Once you have filled or finished creating your classes run python manage.py makemigrations
2. python manage.py migrate
All red unapplied migration errors should now be gone when starting the server

Create Super user to use Django Admin (after migrations only)
1. python manage.py createsuperuser
2. Answer the prompts
3. Turn on server
4. go to 127.0.0.1:8000/admin and use that login info
