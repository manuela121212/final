from django.urls import path
from app_about.views import historia

urlpatterns = [
    path('historia/', historia),
]