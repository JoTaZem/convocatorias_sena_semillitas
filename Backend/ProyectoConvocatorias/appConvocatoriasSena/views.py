from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from smtplib import SMTPException
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib import auth
import string
import random
from django.http import JsonResponse


def home(request):
    return JsonResponse({"mensaje": "Hola mundo desde Django"})


def enviarCorreo(asunto=None, mensaje=None, destinatario=None, archivo=None):
    remitente = settings.EMAIL_HOST_USER
    template = get_template('enviarCorreo.html')
    contenido = template.render({'mensaje': mensaje})

    try:
        # cuerpo en texto plano como fallback
        correo = EmailMultiAlternatives(
            subject=asunto,
            body=mensaje or "Este correo requiere un cliente con soporte HTML.",
            from_email=remitente,
            to=destinatario
        )
        correo.attach_alternative(contenido, "text/html")

        if archivo:
            correo.attach_file(archivo)

        correo.send(fail_silently=False)
        print("Correo enviado correctamente")

    except Exception as e:
        print(f"Error al enviar correo: {e}")


@csrf_exempt
def login(request):
    if request.method == "POST":
        try:
            username = request.POST["txtUser"]
            password = request.POST["txtPassword"]
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                if user.usuRol == "Lider":
                    mensaje = f"Usuario {user.username} con el rol de Líder ha iniciado sesión"
                elif user.usuRol == "Funcionario":
                    mensaje = f"Usuario {user.username} con el rol de Funcionario ha iniciado sesión"
                else:
                    mensaje = f"Usuario {user.username} con el rol de Aprendiz ha iniciado sesión"
            else:
                mensaje = "Usuario o contraseña incorrectas"
        
        except Exception as e:
            mensaje = str(e)

        return JsonResponse({"mensaje": mensaje})
    
    return JsonResponse({"mensaje": "Método no permitido"}, status=405)


def generar_password(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    return password
