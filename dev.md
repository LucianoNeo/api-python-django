# API em PYTHON com DJANGO REST

## Criar Vitual Environment
python3 -m venv ./venv
Fechar o terminal e iniciar novamente

## Dependencias
pip install django djangorestframework
pip install djangorestframework

### Iniciar projeto Django
django-admin startproject config .
django-admin startapp nomeDoApp

### Rodar servidor Django
python manage.py runserver

### Após criar models 
Adicionar o app rest_framework ao settings.py
Adicionar o app ao settings.py
```
python manage.py makemigrations
python manage.py migrate
```

### Criar usuario admin
python manage.py createsuperuser

### Criar serializer
Para poder passar do python para o JSON e vice versa
Arquivo serializer.py
```
from rest_framework import serializers
```

### Criar viewsets
Configura o conteudo disponibilizado no endpoint (equivalente ao controller no js)
Arquivo views.py
```

```

### Criar URLS (endpoint)
Arquivo config/urls.py

## Deploy na heroku

### Dependencias
pip install django-heroku 
pip install gunicorn 

Criar arquivo Procfile
```
web: gunicorn config.wsgi
```

Importar django_heroku no settings.py
```
import django_heroku
django_heroku.settings(locals())
```

## Gerar requirements
pip freeze > requirements.txt