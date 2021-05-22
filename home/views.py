from django.shortcuts import render

from .models import BussinesIncubator, Calibration, Certification, Consultation, Sample, ServiceIndeks, Training


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
    context = {
        'title': 'Layanan BBIHP | Pengujian',
        'sampel_panga': sampel_pangan,
        'sampel_pertanian': sampel_pertanian,
        'sampel_mineral': sampel_mineral,
        'sampel_maritim': sampel_maritim,
        'sampel_lainnya': sampel_lainnya,
    }
    return render(request, 'layanan/pengujian.html', context)


def kalibrasi(request):
    """ Menampilkan kalibrasi """
    semua_alat = Calibration.objects.all()
    context = {
        'title': 'Layanan BBIHP | Kalibrasi',
        'semua_alat': semua_alat
    }
    return render(request, 'layanan/kalibrasi.html', context)


def sertifikasi(request):
    """ Menampilkan sertifikasi """
    context = {
        'title': 'Layanan BBIHP | Sertifikasi'
    }
    return render(request, 'layanan/sertifikasi.html', context)


def kosultasi(request):
    """ Menampilkan konsultasi """
    jasa_konsul = Consultation.objects.all()
    context = {
        'title': 'Layanan BBIHP | Konsultasi',
        'jasa_konsul': jasa_konsul
    }
    return render(request, 'layanan/konsultasi.html', context)


def kerjasama_riset(request):
    """ Menampilkan kerjasama riset """
    context = {
        'title': 'Layanan BBIHP | Kerjasama Riset'
    }
    return render(request, 'layanan/kerjasama_riset.html', context)


def inkubator(request):
    """ Menampilkan inkubator bisinis """
    contex = {
        'title': 'Layanan BBIHP | Inkubator Bisnis'
    }
    return render(request, 'layanan/inkubator.html', contex)


def pelatihan(request):
    """ Menampilkan pelatihan """
    jasa_pelatihan = Training.objects.all()
    contex = {
        'title': 'Layanan BBIHP | Pelatihan',
        'jasa_pelatihan' : jasa_pelatihan
    }
    return render(request, 'layanan/pelatihan.html', contex)
