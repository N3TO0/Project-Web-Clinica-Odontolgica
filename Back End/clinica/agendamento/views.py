from rest_framework import generics
from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario, HorarioDisponivel, Lembrete, Consulta
from .serializers import UsuarioSerializer, HorarioDisponivelSerializer, LembreteSerializer, ConsultaSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class HorarioDisponivelViewSet(viewsets.ModelViewSet):
    queryset = HorarioDisponivel.objects.all()
    serializer_class = HorarioDisponivelSerializer

class LembreteViewSet(viewsets.ModelViewSet):
    queryset = Lembrete.objects.all()
    serializer_class = LembreteSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class UsuarioCreateView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class ConsultaCreateView(generics.CreateAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class ConsultaListView(generics.ListAPIView):
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        cliente_id = self.request.query_params.get('cliente_id')
        return Consulta.objects.filter(cliente_id=cliente_id)