# Baslangic --

    python --version
    python -m venv env
    source ./env/bin/activate
    pip install -r requirements.txt # /ya da/ pip install django
    pip install python-decouple
    pip freeze > requirements.txt
    django-admin startproject main .
    django-admin startapp fscohort /ya da/ python manage.py startapp fscohort
    python manage.py runserver

# App Olusturduktan sonra

--> main > settings.py > INSTALLED_APPS > 'AppName'

# urls.py

--> Import et
form django.http import HttpResponse

--> fonksiyon olustur
def home(request):
    return HttpResponse(''' ''')

--> urlpatterns kismina path ekle
urlpatterns = [
    path('url', func),
    path('fscohort/', include('fscohort.urls')), 
# fscohort/urls.py == fscohort ile baslayan app url lerini kendi yonetmesi icin yol gosterdik
]

# App icerisinde bir urls.py olusturduktan sonra
--> 1. adim
    form django.urls import path
    form .views import fscohort, goodbye 
    |_ views icine fonksiyonlari yaziyoruz ve urls icine import ediyoruz
--> 2.adim
    path yazmak.
# models.py
--> class Student(models.Model):
        fieldname = models.CharField(max_length=50)
        ...
        def __str__(self): #Kayit yazdir.
            return f'{self.first_name} ...'

-->     class Meta:  # Default ozellikleri degistir.
            verbose_name = 'Ogrenci'
            verbose_name_plural = 'Ogrenciler'
            ordering = ["-first_name"] # Ters siralama icin {DESC} sutun isminin basina - konur.

# admin.py
--> 1.adim
    from django.contrib import admin
    form .models import Student

--> 2.adim
    admin.site.register(Student)

# Son adim
    python manage.py makemigrations => yapisal degisiklik yapildiginda modelde kullanilir
    python manage.py migrate

image icin => pip install pillow 

#  Media
    STATIC_URL = 'static/'
    STATIC_ROOT = BASE_DIR / STATIC_URL
    MEDIA_URL = 'media/'
    MEDIA_ROOT = BASE_DIR / MEDIA_URL
     #for MEDIA:
        from django.conf import settings
        from django.conf.urls.static import static
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
