from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def home(request):
    return Response(
        {
            "message": "Welcome to the Home Page"
        }
    )


# ------------------------------------------------------------
'''
    HTTP Request Types:
        Get -> Public verilerdir. Listeleme/Goruntuleme islemlerinde kullanilir.
        Post -> Private verilerdir. Kayit olusturma islemlerinde kullanilir. (ID'ye ihtiyac duymaz.)
        * Put -> Kayit guncelleme islemlerinde kullanilir. (Veri bir butun olarak guncellenir.) (ID'ye ihtiyac duyar.)
        * Patch -> Kayit guncelleme islemlerinde kullanilir. (Verinin sadece ilgili kismi guncellenir.) (ID'ye ihtiyac duyar.)
        * Delete -> Kayit silme islemlerinde kullanilir. (ID'ye ihtiyac duyar.)

'''
# ------------------------------------------------------------
# StudentSeralizers Tum Kayitlari Goruntuleme

from .models import Student

def student_list(request):
    student = Student.objects.all()