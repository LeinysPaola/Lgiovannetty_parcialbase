from django.contrib import admin

from apps.mantenimientos.models import Mantenimiento

# Register your models here.

class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'solicitud','tiempoAtencion')
    ordering = ('fecha', 'solicitud', 'tiempoAtencion')
    search_fields = ('fecha', 'solicitud', 'tiempoAtencion')


admin.site.register(Mantenimiento,MantenimientoAdmin)