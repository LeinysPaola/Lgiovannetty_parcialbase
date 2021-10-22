from django.contrib import admin

from apps.equipos.models import Equipo, EquipoMantenimiento

# Register your models here.

class MembershipInline(admin.TabularInline):
    '''Tabular Inline View for '''

    model = EquipoMantenimiento
   
    extra = 1

class EquipoAdmin(admin.ModelAdmin):
    inlines= (MembershipInline,)    
    list_display = ('nombre', 'marca','modelo')
    ordering = ('nombre', 'marca', 'modelo')
    search_fields = ('nombre', 'marca', 'modelo')
admin.site.register(Equipo, EquipoAdmin)