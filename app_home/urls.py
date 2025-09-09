from django.urls import path
from app_home.views import home

urlpatterns = [
    path('home/', home),
]