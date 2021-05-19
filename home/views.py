from django.shortcuts import render

from .models import BussinesIncubator, Calibration, Consultation, Sample, Service, ServiceIndeks


# Create your views here.
def home(request):
    """Menampilkan halaman beranda, ingin ditambahkan fitur agar indeks kepuasan pelanggan dapat
    ditambahkan dari database"""
    indeks = ServiceIndeks.objects.all()

    context = {
        'title': 'Selamat Datang | BBIHP Kemenperin',
        'indeks': indeks,
    }
    return render(request, 'home/home.html', context)


def profil_bbihp(request):
    """ Menampilkan profil bbihp"""
    context = {
        'title': 'Profil BBIHP'
    }
    return render(request, 'tentang_kami/profil_bbihp1.html', context)


def profil_pejabat(request):
    """ Menampilkan profil bbihp"""
    context = {
        'title': 'Profil Pejabat'
    }
    return render(request, 'tentang_kami/profil_pejabat.html', context)


def pengujian(request):
    """ Menampilkan pengujian """
    sampel_pangan = Sample.objects.filter(kategori='P')
    sampel_pertanian = Sample.objects.filter(kategori='p')
    sampel_mineral = Sample.objects.filter(kategori='m')
    sampel_maritim = Sample.objects.filter(kategori='M')
    sampel_lainnya = Sample.objects.filter(kategori='X')
    contex = {
        'title': 'Layanan BBIHP | Pengujian',
        'sample_pangan': sampel_pangan,
        'sample_pertanian': sampel_pertanian,
        'sample_mineral': sampel_mineral,
        'sample_maritim': sampel_maritim,
        'sample_lainnya': sampel_lainnya,
    }
    return render(request, 'layanan/pengujian.html', contex)


def kalibrasi(request):
    """ Menampilkan kalibrasi """
    contex = {
        'title': 'Layanan BBIHP | Kalibrasi'
    }
    return render(request, 'layanan/kalibrasi.html', contex)


def sertifikasi(request):
    """ Menampilkan sertifikasi """
    contex = {
        'title': 'Layanan BBIHP | Sertifikasi'
    }
    return render(request, 'layanan/sertifikasi.html', contex)
