from rest_framework import generics
from .serializers import convocatoriaSerializer
from .models import *



class ConvocatoriaList(generics.ListCreateAPIView):
    queryset = Convocatoria.objects.all()
    serializer_class = convocatoriaSerializer

class ConvocatoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Convocatoria.objects.all()
    serializer_class = convocatoriaSerializer

