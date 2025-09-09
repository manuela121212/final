from django.urls import path
from app_services.views import pilotos

urlpatterns = [
    path('pilotos/', pilotos),
]