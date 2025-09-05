from django.shortcuts import render
from appConvocatoriasSena.models import Usuario,Funcionario
from django.db import Error,transaction
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from appConvocatoriasSena.views import enviarCorreo, generar_password
import threading


@csrf_exempt
def addFuncionario(request):
    try:
        if request.method == "POST":
            identificacion = request.POST['txtIdentificacion']
            nombre         = request.POST['txtNombre']
            apellido       = request.POST['txtApellido']
            correo         = request.POST['txtCorreo']
            cargo          = request.POST['txtCargo']

            with transaction.atomic():
                usuario = Usuario(
                    usuIdentificacion = identificacion, 
                    first_name        = nombre, 
                    last_name         = apellido, 
                    email             = correo, 
                    usuRol            = "Funcionario", 
                    username          = correo
                    )
                usuario.save()
                usuario.is_active = True
                
                passwordGenerado = generar_password()
                usuario.set_password(passwordGenerado)
                usuario.save()

                funcionario = Funcionario(funCargo=cargo, funUsuario=usuario)
                funcionario.save()

                asunto = "Registro de Usuario en el Sistema"
                mensajeCorreo = f"Cordial Saludo <b>{nombres} {apellidos}</b> usted ha sido registrado\
                en el sistema de Gestion de Convocatorias para aprendices del CTPI SENA Cauca\
                <br><br>nos permtimos enviar las credenciales de ingreso al sistema<br><br>\
                <b>Username:</b> {correo} </br>\
                <b>Password:</b> {passwordGenerado} </br>\
                la URL del sistema es: https://127.0.0.1:8000/"
                thread = threading.Thread(
                    target=enviarCorreo, arg=(asunto, mensajeCorreo, [correo],None))
                thread.start()
            mensaje = "funcionaria agregado correctamente..."
        else:
            mensaje = "No permitido"

    except Error as e:
        transaction.rollback()
        mensaje = e

    retorno = { 
        "mensaje" : mensaje
    }

    return JsonResponse(retorno)