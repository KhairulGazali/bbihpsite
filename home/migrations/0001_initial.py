# Generated by Django 3.1.7 on 2021-04-05 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul_artikel', models.CharField(max_length=25)),
                ('isi_artikel', models.TextField()),
            ],
        ),
    ]