from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    # homepage
    path('', views.home, name='home'),
    # tentang kami
    path('tentang_kami/profil_bbihp/', views.profil_bbihp, name='profil_bbihp'),
    path('tentang_kami/profil_pejabat/', views.profil_pejabat, name='profil_pejabat'),
    # layanan
    path('layanan/pengujian', views.pengujian, name='pengujian'),
    path('layanan/kalibrasi', views.kalibrasi, name='kalibrasi'),
    path('layanan/sertifikasi', views.sertifikasi, name='sertifikasi'),
    path('layanan/konsultasi', views.kosultasi, name='konsultasi'),
    path('layanan/kerjasama_riset', views.kerjasama_riset, name='kerjasama_riset'),
    path('layanan/inkubator', views.inkubator, name='inkubator'),
    path('layanan/pelatihan', views.pelatihan, name='pelatihan'),
]
