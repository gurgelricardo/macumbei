from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.pagina_cadastro, name='pagina_cadastro'),
    path('salvar/', views.salvar_ponto, name='salvar_ponto'),
    path('listar/', views.listar_pontos, name='listar_pontos'),
]
