from django.contrib import admin
from .models import BussinesIncubator, Consultation, Calibration, Sample, Service,  ServiceIndeks,  Training


# Register your models here.

# Home Model
class GoodServiceAdmin(admin.ModelAdmin):
    list_display = ('tahun_pelayanan', 'indeks_kepuasan')


admin.site.register(ServiceIndeks, GoodServiceAdmin)


class SampleAdmin(admin.ModelAdmin):
    list_display = ('nama', 'sni', 'kategori')
    list_filter = ('kategori',)


admin.site.register(Sample, SampleAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nama',)


admin.site.register(Service, ServiceAdmin)


class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('nama',)


admin.site.register(Consultation, ConsultationAdmin)
admin.site.register(BussinesIncubator)
admin.site.register(Training)
admin.site.register(Calibration)
