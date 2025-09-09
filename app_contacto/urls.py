from django.urls import path
from app_contacto.views import contacto, respuesta_contacto

urlpatterns = [
    path('contacto/', contacto),
    path('contacto/respuesta_contacto/', respuesta_contacto),
]