from django.db import models


# Create your models here.
class IndeksKepuasanPelayanan(models.Model):
    tahun_pelayanan = models.IntegerField(default=2020)
    indeks_kepuasan = models.CharField(max_length=10)

    def __str__(self):
        return str(self.tahun_pelayanan)