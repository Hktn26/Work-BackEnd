from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Account)
admin.site.register(Profile)
admin.site.register(Adress)
admin.site.register(Product)