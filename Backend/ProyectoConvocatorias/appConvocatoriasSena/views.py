from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from smtplib import SMTPException
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib import auth

# Create your views here.
#def home(request):
 #   return {"mensaje":"Hola mundo desde Django"}
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
                    mensaje = f"Usuario {user.username} con el rol de Lider ha iniciado la sesion"
                elif user.usuRol == "Funcionario":
                    mensaje = f"Usuario {user.username} con el rol de Funcionario ha iniciado la sesion"
                else:
                    mensaje = f"Usuario {user.username} con el rol de Aprendiz ha iniciado la sesion"
            else:
                mensaje = "Usuario o contrasena incorrectas"
        
        except Exception as e:
            mensaje = str(e)

        retorno = {
            "mensaje" : mensaje
        }
            
    return JsonResponse(retorno)