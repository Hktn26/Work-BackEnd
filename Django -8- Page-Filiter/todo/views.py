
from rest_framework.viewsets import ModelViewSet
from .serializers import Todo, TodoSerializer
# Alternatif gecici yontem:
# from rest_framework.pagination import PageNumberPagination
from .paginations import (
    CustomPageNumberPagination,
    CustomLimitOffsetPahination,
    CustomCursorPagination
)

# Django filitreleme modulu
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class TodoView(ModelViewSet):
    queryset = Todo.objects.all().order_by('title')
    serializer_class = TodoSerializer
    # filitreleme modulleri:
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter] # local filiter settings.
    # Filter: Birebir eslestirme
    filterset_fields = ['id','priority','is_done']
    #Search: Icinde arama
    # https://www.django-rest-framework.org/api-guide/filtering/#searchfilter
    search_fields = ['title', 'description']
    # Ordering: Siralama
    ordering_fields = ['id', 'title'] # '__all__'
    # --------------------------------------------------------------
   
    # pagination_class = CustomPageNumberPagination  # Local Settings:
    # pagination_class = CustomCursorPagination  # Local Settings:
    # pagination_class = CustomLimitOffsetPahination  # Local Settings:

    # Alternatif gecici (veya sadece bu classs icin calisan) yontem:
    # pagination_class = CustomPageNumberPagination
    # PageNumberPagination.page_size = 25
    # PageNumberPagination.page_size_query_parm = 'Adet' # URL ile kac adet gonderilecegini belirleyebilirim
    # PageNumberPagination.page_query_param = 'Sayfa' #Page ismini degistirdik

'''
# Manuel arama ornegi:
    # Override:
    def get_queryset(self):
        # URL'den parametre degerini yakala:
        title = self.request.query_params.get('title')
        if title is None:
            # Arama yapma parametre yok
            return super().get_queryset()
        else:
            # Arama yap
            # queryset icinde ara:
            return self.queryset.filter(title__contains=title)  # filitreleme
'''

