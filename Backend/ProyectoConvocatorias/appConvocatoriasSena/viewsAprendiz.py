from django.shortcuts import render
from appConvocatoriasSena.models import Convocatoria,Postulacion,Usuario,Aprendiz
from django.db import Error,transaction
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from appConvocatoriasSena.views import generar_password,enviarCorreo
import threading

formato_fecha = "%Y/%m/%d %H:%M:%S"

@csrf_exempt
def addAprendiz(request):
    try:
        if request.method=="POST":
            identificacion = request.POST["txtIdentificacion"]
            nombres = request.POST["txtNombres"]
            apellidos = request.POST["txtApellidos"]
            correo = request.POST["txtCorreo"]
            ficha = request.POST["txtFicha"]
            programa = request.POST["txtPrograma"]
        
            with transaction.atomic():
                usuario = Usuario(
                    usuIdentificacion=identificacion,
                    first_name = nombres, last_name = apellidos,
                    email = correo, usuRol="Aprendiz",
                    username=correo
                )
                usuario.save()
                usuario.is_active = True
                passwordGenerado = generar_password()
                usuario.set_password(passwordGenerado)
                usuario.save()
                aprendiz = Aprendiz(
                    aprFicha=ficha,aprPrograma=programa,
                    aprUsuario=usuario
                )
                aprendiz.save()
                asunto = "Registro de Usuario en el Sistema"
                mensajeCorreo = f"Cordial Saludo aprendiz <b>{nombres} {apellidos}</b> usted ha sido registrado\
                en el sistema de Gestion de Convocatorias para aprendices del CTPI SENA Cauca\
                <br><br>nos permtimos enviar las credenciales de ingreso al sistema<br><br>\
                <b>Username:</b> {correo} </br>\
                <b>Password:</b> {passwordGenerado} </br>"
                thread = threading.Thread(
                    target=enviarCorreo, arg=(asunto, mensajeCorreo, [correo],none))
                thread.start()
            mensaje="Aprendiz Agregado Correctamente..."
        else:
            mensaje = "no permitido"
    except Error as error:
        transaction.rollback
        mensaje = error
    retorno = {"mensaje":mensaje,"username":correo,"password":passwordGenerado}    
    return JsonResponse(retorno)

