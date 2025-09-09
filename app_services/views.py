from django.shortcuts import render
from app_services.models import Pilotos

# Create your views here.
def pilotos(request):
    p = Pilotos.objects.all()
    return render(request, 'app_services/services.html', {'piloto': p})