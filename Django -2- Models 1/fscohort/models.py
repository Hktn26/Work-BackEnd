from django.db import models

# Create your models here.

# Referans
# https://docs.djangoproject.com/en/4.2/topics/db/models/


class Student(models.Model):
    # https://docs.djangoproject.com/en/4.2/ref/models/fields/
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.IntegerField()
    is_active = models.BooleanField(default=True)
    # image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True) # Kayit yapildigi anki zamani otomatik yaz
    updated = models.DateTimeField(auto_now=True)  # Kaydi guncellendigi anki zamani otomatik yaz

    def __str__(self):
        return f'{self.first_name} {self.last_name} # {self.number}'
    
    # https://docs.djangoproject.com/en/4.2/ref/models/options/
    class Meta: # Default ozellikleri degistir.
        verbose_name = 'Ogrenci'
        verbose_name_plural = 'Ogrenciler'
        ordering = ["number"] # Ters siralama icin {desc} sutun isminin basina -konur.
