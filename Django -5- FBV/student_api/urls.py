from django.urls import path
from .views import (
    home,
    student_list,
    student_create,
    student_detail,
    student_update,
    student_delete,
    student_list_create,
)

urlpatterns = [
    path('', home),
    path('student_list/', student_list),  # listeleme
    path('student_create/', student_create),  # kayit
    path('student_detail/<int:pk>', student_detail),  # Tek-Kayit Goruntuleme
    path('student_update/<int:pk>', student_update),  # Tek-Kayit Guncelleme
    path('student_delete/<int:pk>', student_delete),  # Tek-Kayit Silme
    path('student_list_create/', student_list_create),
]
