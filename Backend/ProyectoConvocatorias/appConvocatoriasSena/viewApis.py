from rest_framework import generics
from .serializers import convocatoriaSerializer
from .models import *



class convocatoriaSerializer(serializers.ListCreateAPIView):
    queryset = Convocatoria.objects.all()
    serializer_class = convocatoriaSerializer
    
    class creatorDetailsSerializer(serializers.ModelSerializer):
        queryset = Convocatoria.objects.all()
        serializer_class = convocatoriaSerializer
        
        