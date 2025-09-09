from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def contacto(request):
    return render(request, 'app_contacto/contact.html')

# Enviar info al correo
def respuesta_contacto(request):
    if request.method == 'POST':
        name = request.POST['nombre']
        message = f"{request.POST['mensaje']}\n\nEmail de contacto: {request.POST['email']}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['manuela180707@gmail.com']

        send_mail(name, message, from_email, recipient_list)
        return render(request, 'app_contacto/respuesta_form.html')
    return render(request, 'app_contacto/contact.html')