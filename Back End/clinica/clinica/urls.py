from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Apenas uma vez
    path('api/', include('agendamento.urls')),  # Rota para o app agendamento
]
