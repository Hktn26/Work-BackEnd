# Django Session - 1

# Framework nedir?

    Çerçeveler, belirli bir programlama dili veya yazılım platformu için yeniden kullanılabilir kod sağlayan yazılım bileşenleridir. Genellikle belirli bir görevi yerine getirmek için kullanılabilen önceden tanımlanmış sınıflar, işlevler ve değişkenler içerirler. Çerçeveler, yazılım geliştirmeyi hızlandırmaya ve karmaşıklığı azaltmaya yardımcı olabilir.

    Django, Python ile yazılmış bir web uygulaması geliştirmek için

# Django nedir?

    Django, Python'da web uygulamaları geliştirmek için kullanılan bir çerçevedir. Model-View-Controller (MVC) mimari desenine dayanır ve hızlı, güvenli ve bakımı kolay web siteleri oluşturmayı kolaylaştırır. Django, karmaşık web siteleri oluşturmak için gereken birçok özelliği ve işlevi içerir


    pip install module_name
    pip uninstall module_name
    pip list
    pip freeze

# Insatll DJANGO

    pip install django
    django-admin --version
    django-admin startproject projectName .
    django-admin startapp appName

# Run Django

    python --version
    python -m venv env
    source ./env/Scripts/activate
    deactivate => yapinca cikiyon
    python manage.py runserver
    ctrl + C => stop server

# DB Migrate

    python manage.py migrate

# Create SuperUser

    python manage.py createsuperuser

2.39 dan sonra MVT ve MVC nin teorisini anlatiyor.

# RunServer yap ve git.
# Go to adminpanel http://127.0.0.1:8000/admin/ 

# MVC: Model View Controller

    Model : Veri Tabanina erismeyi saglayan kismi (Database)
    View : Gosterim Kismi (Template)
    Controller : Islem Yapan Kismi (URL Dispatcher)

# MVT nedir?

    Model : Veri Tabanina Erismeyi Saglayan Kismi (Database)
    View : Gosterme Kismi (Template)
    Templte : Gostermek icin Kullanilacak HTML veya XML dosyalarindan olusur.

# Create a new Project

django-admin startproject mysite .

# Start App

django-admin startapp polls

# Run Server

python manage.py runserver

# Open Browser and go to http://localhost:8000/

# Installing apps

python manage.py makemigrations
python manage.py migrate

# Creating admin user

python manage.py createsuperuser

# Django Templates Language

{% extends "base_generic.html" %} # extend the base template
{% block content %} {% endblock content %}

# Static Files

STATIC_URL = '/static/'
INSTALLED_APPS = [
'polls',
]

# Collect static files

python manage.py collectstatic
