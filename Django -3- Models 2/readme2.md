python -m venv env
source env/Scripts/activate
pip install django
pip freeze
pip freeze > requirements.txt
pip install -r requirements.txt # requairements.txt icindeki tum modulleri yukler
django-admin startproject main .
django-admin startapp fscohort
python manage.py runserver
python manage.py migrate
python manage.py createsuperuser
python manage.py makemigrations ->django da yaptigim degisiklikleri algila

urls.py -> 