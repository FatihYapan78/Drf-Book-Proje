from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator


class Kitap(models.Model):
    isim = models.CharField(max_length=50)
    yazar = models.CharField(max_length=50)
    aciklama = models.TextField()
    eklenme_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)
    yayin_tarihi = models.DateTimeField()

    def __str__(self):
        return f'{self.isim} - {self.yazar}'

class Yorum(models.Model):
    kitap = models.ForeignKey(Kitap, related_name="yorumlar", on_delete=models.CASCADE)
    yorumcu = models.CharField(max_length=50)
    yorum = models.TextField()
    eklenme_tarihi = models.DateTimeField(auto_now_add=True)
    guncelleme_tarihi = models.DateTimeField(auto_now=True)
    degerlendirme = models.PositiveIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
    )

    def __str__(self):
        return str(self.kitap)