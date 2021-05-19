from django.db import models


# Create your models here.
class ServiceIndeks(models.Model):
    tahun_pelayanan = models.IntegerField(default=2020)
    indeks_kepuasan = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        ordering = ['-tahun_pelayanan']

    def __str__(self):
        return str(self.tahun_pelayanan)


class Sample(models.Model):
    nama = models.CharField(max_length=200, help_text='Mohon memasukkan nama sample sesuai format (ex: Biji Kakao)')
    sni = models.CharField('Nomor SNI', max_length=100, default='SNI - ',
                           help_text='Mohon memasukkan no. SNI yang benar sesuai format (ex: SNI 2323 '
                                     ': 2008')
    CATEGORY = (
        ('p', 'Pertanian'),
        ('P', 'Pangan'),
        ('m', 'Mineral'),
        ('M', 'Maritim'),
        ('X', 'Lain-Lain'),
    )
    kategori = models.CharField(max_length=1, choices=CATEGORY, default='X')

    def __str__(self):
        return str(self.nama)


class Calibration(models.Model):
    nama = models.CharField(max_length=200)
    keterangan = models.TextField()

    def __str__(self):
        return str(self.nama)


class Service(models.Model):
    nama = models.CharField(max_length=200)
    sample = models.ManyToManyField(Sample, help_text='Pilih jenis layanan')
    keterangan = models.TextField(blank=True, null=True, help_text='Masukkan keterangan sampel')

    def __str__(self):
        return str(self.nama)


class Consultation(models.Model):
    nama = models.CharField(max_length=200, )
    keterangan = models.TextField(blank=True, null=True, help_text='Masukkan keterangan topik konsultasi')

    def __str__(self):
        return str(self.nama)


class BussinesIncubator(models.Model):
    klien = models.CharField(max_length=200, )
    alamat = models.TextField(blank=True, null=True, help_text='Masukkan keterangan sampel')
    keterangan = models.TextField(blank=True, null=True, help_text='Masukkan keterangan sampel')

    def __str__(self):
        return str(self.klien)


class Training(models.Model):
    nama = models.CharField(max_length=200)
    keterangan = models.TextField(blank=True, null=True, help_text='Masukkan keterangan pelatihan')

    def __str__(self):
        return str(self.nama)
