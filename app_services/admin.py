from django.contrib import admin
from app_services.models import Pilotos

# Register your models here.
class PilotosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'equipo', 'imagen', 'campeonatos')

admin.site.register(Pilotos, PilotosAdmin)
