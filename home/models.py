from django.db import models


# Create your models here.
class ServiceIndeks(models.Model):
    tahun_pelayanan = models.IntegerField(default=2020)
    indeks_kepuasan = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        ordering = ['-tahun_pelayanan']
        verbose_name_plural = "Indeks Pelayanan"

    def __str__(self):
        return str(self.tahun_pelayanan)


class Sample(models.Model):
    nama = models.CharField(max_length=200, unique=True, help_text='Mohon memasukkan nama sample sesuai format (ex: '
                                                                   'Biji Kakao)')
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
        return self.nama


class Calibration(models.Model):
    nama = models.CharField(max_length=200, unique=True)
    keterangan = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Kalibrasi"

    def __str__(self):
        return self.nama


class Certification(models.Model):
    nama = models.CharField(max_length=200, unique=True)
    keterangan = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Sertifikasi"

    def __str__(self):
        return self.nama


class Consultation(models.Model):
    nama = models.CharField(max_length=200, unique=True)
    keterangan = models.TextField(blank=True, null=True, help_text='Masukkan keterangan topik konsultasi')

    class Meta:
        verbose_name_plural = "Konsultasi Teknologi"

    def __str__(self):
        return self.nama[:15]


class BussinesIncubator(models.Model):
    klien = models.CharField(max_length=200, unique=True)
    alamat = models.TextField(blank=True, null=True, help_text='Masukkan keterangan sampel')
    keterangan = models.TextField(blank=True, null=True, help_text='Masukkan keterangan sampel')

    class Meta:
        verbose_name_plural = "Inkubator Bisnis"

    def __str__(self):
        return self.klien


class Training(models.Model):
    nama = models.CharField(max_length=200, unique=True)
    keterangan = models.TextField(blank=True, null=True, help_text='Masukkan keterangan pelatihan')

    class Meta:
        verbose_name_plural = "Pelatihan"

    def __str__(self):
        return self.nama
