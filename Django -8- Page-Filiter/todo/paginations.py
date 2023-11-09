# Local Settings:
from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'adet'
    page_query_param = 'sayfa'