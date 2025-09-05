from django.shortcuts import render
from appConvocatoriasSena.models import Convocatoria,Postulacion,Usuario,Aprendiz
from django.db import Error,transaction
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from appConvocatoriasSena.views import generar_password,enviarCorreo


