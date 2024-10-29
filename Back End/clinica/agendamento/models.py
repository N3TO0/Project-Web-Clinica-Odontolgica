from django.db import models
from uuid import uuid4

# Create your models here.

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    data_de_nascimento = models.DateField()
    senha = models.CharField(max_length=255)  # A senha será armazenada com hash
    TIPO_CHOICES = (
        ('cliente', 'Cliente'),
        ('gestao', 'Gestão'),
    )
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

# Horários Disponíveis
class HorarioDisponivel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    data = models.DateField()
    hora = models.TimeField()
    disponivel = models.BooleanField(default=True)

# Lembretes
class Lembrete(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    consulta = models.ForeignKey('Consulta', on_delete=models.CASCADE, related_name='lembretes')
    data_envio = models.DateTimeField()
    STATUS_CHOICES = (
        ('enviado', 'Enviado'),
        ('pendente', 'Pendente'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

# Consultas
class Consulta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='consultas_cliente')
    profissional = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='consultas_profissional')
    data_consulta = models.DateField()
    horario_consulta = models.TimeField()
    STATUS_CHOICES = (
        ('marcada', 'Marcada'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
