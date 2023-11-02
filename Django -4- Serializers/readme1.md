# serializers nedir django ?
    Serializers, ne Django Rest Framework (DRF) uygulamalarında kullanılan veri aktarımının bir parçasıdır. Bunlar, sorgu parametreleri, üstbilgi, ve yükleri dahil olmak üzere HTTP isteklerinden gelen ve HTTP yanıtlarına giden verileri dönüştürmeye yönelik küçük ve büyük nesnelere (özellikle Python sınıfları ve Django Modelleri) çevirme işlevleri sağlar.

    DRF ile, REST API'nın kolay ve basit bir şekilde tasarlanmasını ve uygulanmasını sağlayan birçok fayda var. Örneğin, REST API'nın geri kalanı ile bağlantılı kalabilmek için otomatik olarak istekleri doğrulama ve serileştirme desteği sunar.


# pip install python-decouple
|-> .env dosyasi olustur
|-> settings.py a git "from decouple import config" yaz
|-> settings.py a git ve "SECRET_KEY = config('SECRET_KEY')" yaz 

# pip install djangorestframework

    --->  https://www.django-rest-framework.org/api-guide/serializers/

model > serializer > view > url