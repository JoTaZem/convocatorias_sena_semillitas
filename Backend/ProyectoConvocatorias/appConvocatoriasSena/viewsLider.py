from django.shortcuts import render
from appConvocatoriasSena.models import Convocatoria,TipoConvocatoria
from django.db import Error,transaction
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

formato_fecha="%Y-%m-%d %H:%M:%S"

@csrf_exempt
def addConvocatoria(request):
    try:
        nombre = request.POST['txtNombre']
        idTipo = request.POST["cbTipoConvocatoria"]
        tipo = TipoConvocatoria.objects.get(pk=idTipo)
        cantidadBeneficiarios = request.POST["txtCantidadBeneficiarios"]
        fechaInicio = request.POST["txtFechaInicio"]
        fecha_inicio = datetime.strptime(fechaInicio,formato_fecha)
        fechaFin = request.POST["txtFechaFin"]
        fecha_fin = datetime.strptime(fechaFin,formato_fecha)
        documento = request.FILES['fileDocumento '] if 'fileDocumento' in request.FILES else None

        convocatoria= Convocatoria(
            conNombre = nombre,
            conTipo = tipo,
            conCantidadBeneficiarios = cantidadBeneficiarios,
            conFechaInicio = fecha_inicio,
            conFechaFinal = fecha_fin,
            conDocumento = documento,
        )
        convocatoria.save()
        mensaje = "Convocatoria registrada correctamente"
    except Error as error:
        mensaje = "Error al registrar la convocatoria: "+str(error)
    retorno={"mensaje":mensaje}
    return JsonResponse(retorno)

