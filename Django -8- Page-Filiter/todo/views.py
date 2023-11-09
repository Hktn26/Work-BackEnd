
from rest_framework.viewsets import ModelViewSet
from .serializers import Todo, TodoSerializer
# Alternatif gecici yontem:
# from rest_framework.pagination import PageNumberPagination
from .paginations import CustomPageNumberPagination


class TodoView(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = CustomPageNumberPagination # Local Settings:

    # Alternatif gecici yontem:
    # pagination_class = CustomPageNumberPagination
    # PageNumberPagination.page_size = 25
    # PageNumberPagination.page_size_query_parm = 'Adet' # URL ile kac adet gonderilecegini belirleyebilirim
    # PageNumberPagination.page_query_param = 'Sayfa' #Page ismini degistirdik
