from django.urls import path
from .views import fscohort, goodbye #basindaki tek nokta ayni klasorde oldugunu gosterir.

# after '/fscohort/'
urlpatterns = [ 
    path('', fscohort),
    path('goodbye/', goodbye)
]
