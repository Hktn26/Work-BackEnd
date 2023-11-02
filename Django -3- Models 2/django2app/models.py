from django.db import models

# Create your models here.


# Referans
# https://docs.djangoproject.com/en/4.2/topics/db/models/
class Student(models.Model):
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(default='none@cw.com', null=True, blank=True)
    number = models.IntegerField(default=0, null=True, blank=True)
    picture = models.ImageField(upload_to='images/', default='', blank=True)
    is_active = models.BooleanField(default=True)
    # image = models.ImageField()
    # Kayit yapildigi anki zamani otomatik yaz
    created = models.DateTimeField(auto_now_add=True)
    # Kaydi guncellendigi anki zamani otomatik yaz
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.picture} {self.first_name} {self.last_name} # {self.number}'

    # https://docs.djangoproject.com/en/4.2/ref/models/options/
    class Meta:  # Default ozellikleri degistir.
        verbose_name = 'Ogrenci'
        verbose_name_plural = 'Ogrenciler'
        # Ters siralama icin {desc} sutun isminin basina -konur.
        ordering = ["number"]

#------------------Django Shell---------

AGES = (
    (10, 'Yas: 10'),
    (20, 'Yas: 20'),
    (30, 'Yas: 30'),
    (40, 'Yas: 40'),
    (50, 'Yas: 50'),
)

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0, blank=True, null=True, choices=AGES)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name} # {self.age}'
    