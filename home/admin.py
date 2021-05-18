from django.contrib import admin
from .models import IndeksKepuasanPelayanan


# Register your models here.

# Home Model
class IndeksKepuasanAdmin(admin.ModelAdmin):
    list_display = ('tahun_pelayanan',)


admin.site.register(IndeksKepuasanPelayanan, IndeksKepuasanAdmin)
