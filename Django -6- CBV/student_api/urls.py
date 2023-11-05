from django.urls import path

from .views import (
    StudentListCreate,
)

urlpatterns = [
    path('student_list_creat/', StudentListCreate.as_view()),
]
