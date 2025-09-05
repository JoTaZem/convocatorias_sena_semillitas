from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from smtplib import SMTPException

# Create your views here.
def home(request):
    return {"mensaje":"Hola mundo desde Django"}

def enviarCorreo(asunto=None, mensaje=None, destinatario=None, archivo=None):
    remitente = settings.EMAIL_HOST_USER
    template = get_template('enviarCorreo.html')
    contenido = template.render({
        'mensaje' : mensaje
    })
    try:
        correo = EmailMultiAlternatives(
            asunto, mensaje, remitente, destinatario
        )
        correo.attach_alternative(contenido, "text/html")
        if archivo != None:
            correo.attach_file(archivo)
        correo.send(fail_silently=True)


    except SMTPException as e:
        print(e)

