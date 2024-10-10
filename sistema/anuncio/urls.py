from django.urls import path
from anuncio.views import ListarAnuncios, CriarAnuncios, EditarAnuncios, DeletarAnuncios, FotoAnuncio

urlpatterns = [
    path('', ListarAnuncios.as_view(), name='listar-anuncios'),
    path('novoA/', CriarAnuncios.as_view(), name='criar-anuncios'),
    path('fotos/<str:arquivo>/', FotoAnuncio.as_view(), name='foto-anuncio'),
    path('<int:pk>/', EditarAnuncios.as_view(), name='editar-anuncios'),
    path('deletarA/<int:pk>', DeletarAnuncios.as_view(), name='deletar-anuncios'),
]