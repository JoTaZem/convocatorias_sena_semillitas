from rest_framework import generics
from .serializers import convocatoriaSerializer, AprendizSerializer, TipoConvocatoriaSerializer
from .models import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .views import *
import threading

class TipoConvocatoriaList(generics.ListCreateAPIView):
    queryset = TipoConvocatoria.objects.all()
    serializer_class = TipoConvocatoriaSerializer

class TipoConvocatoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoConvocatoria.objects.all()
    serializer_class = TipoConvocatoriaSerializer

class ConvocatoriaList(generics.ListCreateAPIView):
    queryset = Convocatoria.objects.all()
    serializer_class = convocatoriaSerializer

    def create(self, request, *args, **kwargs):
        print(request.FILES)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(
                {
                    'mensaje' : 'Convocatoria creada correctamente',
                    'data' : serializer.data
                },
                status = status.HTTP_201_CREATED
            )
        else:
            return Response(
                {
                    'mensaje' : 'Error al guardar la convocatoria',
                    'data' : serializer.errors
                },
                status = status.HTTP_400_BAD_REQUEST
            )


class ConvocatoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Convocatoria.objects.all()
    serializer_class = convocatoriaSerializer

class AprendizList(generics.ListCreateAPIView):
    queryset = Aprendiz.objects.all()
    serializer_class = AprendizSerializer
    pemission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            aprendiz = serializer.instance

            password_generado = generar_password()
            aprendiz.aprUsuario.set_password(password_generado)
            aprendiz.aprUsuario.save()

            asunto = "Registro de Usuario en el Sistema"
            mensajeCorreo = f"Cordial Saludo aprendiz <b>{aprendiz.aprUsuario.first_name} {aprendiz.aprUsuario.last_name}</b> usted ha sido registrado\
            en el sistema de Gestion de Convocatorias para aprendices del CTPI SENA Cauca\
            <br><br>nos permtimos enviar las credenciales de ingreso al sistema<br><br>\
            <b>Username:</b> {correo} </br>\
            <b>Password:</b> {passwordGenerado} </br>"
            thread = threading.Thread(
                target=enviarCorreo, arg=(asunto, mensajeCorreo, [correo],None))
            thread.start()
            return Response(
                {
                    'mensaje' : 'Aprendiz creado correctamente',
                    'data' : serializer.data
                },
                status = status.HTTP_201_CREATED
            )
        else:
            return Response(
                {
                    'mensaje' : 'Error al guardar el aprendiz',
                    'data' : serializer.errors
                },
                status = status.HTTP_400_BAD_REQUEST
            )

class AprendizDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aprendiz.objects.all()
    serializer_class = AprendizSerializer