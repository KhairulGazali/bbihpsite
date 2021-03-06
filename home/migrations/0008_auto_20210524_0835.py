# Generated by Django 3.1.7 on 2021-05-24 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210522_2126'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bussinesincubator',
            options={'verbose_name_plural': 'Inkubator Bisnis'},
        ),
        migrations.AlterModelOptions(
            name='calibration',
            options={'verbose_name_plural': 'Kalibrasi'},
        ),
        migrations.AlterModelOptions(
            name='certification',
            options={'verbose_name_plural': 'Sertifikasi'},
        ),
        migrations.AlterModelOptions(
            name='consultation',
            options={'verbose_name_plural': 'Konsultasi Teknologi'},
        ),
        migrations.AlterModelOptions(
            name='serviceindeks',
            options={'ordering': ['-tahun_pelayanan'], 'verbose_name_plural': 'Indeks Pelayanan'},
        ),
        migrations.AlterModelOptions(
            name='training',
            options={'verbose_name_plural': 'Pelatihan'},
        ),
    ]
