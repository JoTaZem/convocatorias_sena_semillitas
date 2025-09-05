from rest_framework import serializers
from .models import *

class convocatoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convocatoria
        fields = '__all__'
        depth = 1
    