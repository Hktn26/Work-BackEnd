from django.contrib import admin

# Register your models here.
from .models import Student, Customer
admin.site.register(Student)
admin.site.register(Customer)