from django.urls import path

from .views import (
    StudentListCreate,
    StudentDetailUpdateDelete,
    StudentGenericListCreate,
    StudentListCreateAPIView,
    StudentRetrieveUpdateDestroyAPIView,
    StudentViewSet,
)

urlpatterns = [
    path('student_list_creat/', StudentListCreate.as_view()),
    path('student_detail_update_delete/<int:pk>', StudentDetailUpdateDelete.as_view()),
    path('StudentGenericListCreate/', StudentGenericListCreate.as_view()),
    path('StudentListCreateAPIView/', StudentListCreateAPIView.as_view()),
    path('StudentRetrieveUpdateDestroyAPIView/<int:pk>', StudentRetrieveUpdateDestroyAPIView.as_view()),
    path('StudentViewSet/<int:pk>', StudentViewSet.as_view()),
]



# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Router for ModelViewSet

from .views import StudentMVS
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentMVS)  # URL sonunda/ yok.
# Add to paths:
urlpatterns += router.urls