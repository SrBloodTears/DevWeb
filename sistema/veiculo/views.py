from django.shortcuts import render
from django.views.generic import ListView
from veiculo.models import Veiculo

class ListarVeiculos(ListView):
    """
    View para listar veiculos cadastrados.
    """
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'
