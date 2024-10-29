from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, HorarioDisponivelViewSet, LembreteViewSet, ConsultaViewSet, CustomAuthToken, ConsultaListView

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'horarios', HorarioDisponivelViewSet)
router.register(r'lembretes', LembreteViewSet)
router.register(r'consultas', ConsultaViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Inclui todas as rotas do DefaultRouter
    path('login/', CustomAuthToken.as_view(), name='login'),  # Rota personalizada para login
    path('consultas/list/', ConsultaListView.as_view(), name='consulta-list'),  # Rota personalizada para listar consultas
]