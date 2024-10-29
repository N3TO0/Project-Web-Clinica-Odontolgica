from rest_framework import serializers
from .models import Usuario, HorarioDisponivel, Lembrete, Consulta
from django.contrib.auth.hashers import make_password

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'cpf', 'data_de_nascimento', 'senha', 'tipo'] # Removido 'telefone'

    def create(self, validated_data):
        validated_data['senha'] = make_password(validated_data['senha'])
        return super().create(validated_data)

class HorarioDisponivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioDisponivel
        fields = '__all__'

class LembreteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lembrete
        fields = '__all__'

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['id', 'cliente', 'profissional', 'data_consulta', 'horario_consulta', 'status']
