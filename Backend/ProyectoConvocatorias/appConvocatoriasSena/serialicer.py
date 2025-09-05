from rest_framework  import serializers
from .models import Convocatoria

class convocatoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convocatoria
        fields = '__all__'
        depth = 1 # par poder relacionarlos 