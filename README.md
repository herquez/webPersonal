# Personal Website | Django

## About

Project from a course about django, the web framework from python.
This is a personal web site that shows my own projects administrated from a database using the django's panel control.

## Installations

### In machine

- python 3 or later
- pip
- pipenv

### Packages

All packages must be installed into the virtual enviroment. You are able to use de the next bash command followed by the package name.

```bash
pipenv install <package_name>
```

| Package | Description |
|--------------|-------------------------------|
|django| |
|django-ckeditor| |
|Pillow| |
|pylint| |
|pylint-django| |
|pylint-celery| |

### Initial migrations

To create and update the database connected through the settings.py is necessary follow the next commands in order to migrate changes from the models in our project to the respective database.

#### Make migrations

```bash
python manage.py makemigrations
```

#### Migrate

```bash
python manage.py migrate
```
