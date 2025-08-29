from django.shortcuts import render
from appConvocatoriasSena.models import Usuario,Funcionario
from django.db import Error,transaction
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

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
                usuario = Usuario(usuIdentificacion=identificacion, first_name = nombre, last_name = apellido, email=correo, usuRol="Funcionario", username = correo)
                usuario.save()
                usuario.is_active = True
                usuario.set_password("12345")

                funcionario = Funcionario(funCargo=cargo, funUsuario=usuario)
                funcionario.save()
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