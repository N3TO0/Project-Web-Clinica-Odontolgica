from django.contrib import admin
from .models import Usuario, HorarioDisponivel, Lembrete, Consulta

# Register your models here.
admin.site.register(Usuario)
admin.site.register(HorarioDisponivel)
admin.site.register(Lembrete)
admin.site.register(Consulta)