# Project STR-TO-VID
This is a small application that creates a running text line video from a text string.

Getting started:
```
Fork the repository and clone it to the desired location:
    git clone...
Set up a virtual environment:
    python -m venv venv
Install libraries from the requirements.txt file to the virtual environment:
    (venv) pip install -r requirements.txt
Run migrations:
    (venv) python manage.py migrate
Start the application:
    (venv) python manage.py runserver
```

Usage:
```
Creating a superuser to access the Django admin panel:
    python manage.py createsuperuser
Creating videos:
    Just enter the text into the box on the title page
```
Database:
```
if you wish to use the postgreSQL database for the project:
    The application is already setup to work with a
    database name: videodb
    user name: django_admin
    and password: django_pass
    Just uncomment the corresponding code in settings.py
```

