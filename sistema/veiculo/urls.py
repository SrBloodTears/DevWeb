from django.urls import path
from veiculo.views import ListarVeiculos, FotoVeiculo, CriarVeiculos

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='Listar-veiculos'),
    path('novo/', CriarVeiculos.as_view(), name='criar-veiculos'),
    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name='foto-veiculo'),
]