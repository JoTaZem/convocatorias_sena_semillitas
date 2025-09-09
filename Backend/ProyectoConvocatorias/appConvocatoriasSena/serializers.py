from rest_framework import serializers
from .models import *

class TipoConvocatoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoConvocatoria
        fields = '__all__'
        depth = 2

class convocatoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convocatoria
        fields = '__all__'
        depth = 2

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        depth = 2
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Usuario(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        return user

class AprendizSerializer(serializers.ModelSerializer):
    aprUsuario = UsuarioSerializer()

    class Meta:
        model = Aprendiz
        fields = '__all__'

    def create(self, validated_data):
        usuario_data = validated_data.pop('aprUsuario')
        usurio = UsuarioSerializer().create(usuario_data)
        aprendiz = Aprendiz.objects.create(aprUsuario=usurio, **validated_data)
        return aprendiz