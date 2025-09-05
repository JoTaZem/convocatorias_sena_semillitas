from django.shortcuts import render
from appConvocatoriasSena.models import Convocatoria,TipoConvocatoria, Aprendiz, Postulacion
from django.db import Error,transaction
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import threading
from appConvocatoriasSena.views import enviarCorreo


@csrf_exempt
def postulacion(request):
    try:
        if request.method == "POST":
            convocatoria = Convocatoria.objects.get(pk=1)
            aprendiz = Aprendiz.objects.get(pk = 1)

            with transaction.atomic():
                postulacion = Postulacion(posAprendiz=aprendiz, posConvocatoria=convocatoria)
                postulacion.save()

                asunto = "Postulacion convocatorias Bienestar Aprendices"
                mensajeCorreo = f"Cordial saludo aprendiz<b>{aprendiz.aprUsuario.first_name}\
                    {aprendiz.aprUsuario.last_name} </b>, nos permitimos confirmar su postulacion \
                    a la convocatoria de nombre: <b>{convocatoria.conNombre.upper()}</b>.\
                        <br><br>Le recorfamos estar pendiente de los resultados"

                thread = threading.Thread(
                    target = enviarCorreo, args = (asunto, mensajeCorreo, [aprendiz.aprUsuario.email], None)
                )
                thread.start()
                mensaje = "Postulacion registrada correctamente"
        else:
            mensaje = "No permitido"

    except Error as e:
        transaction.rollback()
        mensaje = e

    retorno = { 
        "mensaje" : mensaje
    }

    return JsonResponse(retorno)