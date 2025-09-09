from django.shortcuts import render

# Create your views here.
def historia(request):
    return render(request, 'app_about/about.html')