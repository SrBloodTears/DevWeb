from django.views.generic import View
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from veiculo.models import Veiculo
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from veiculo.form import FormularioVeiculo

class ListarVeiculos(LoginRequiredMixin, ListView):
    """
    View para listar veiculos cadastrados.
    """
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'

class CriarVeiculos(LoginRequiredMixin, CreateView):
    """
    View para criar veiculos.
    """
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculos')

class EditarVeiculos(LoginRequiredMixin, UpdateView):
    """
    View para a edição de veiculos já cadastrados
    """
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/editar.html'
    success_url = reverse_lazy('listar-veiculos')

class DeletarVeiculos(LoginRequiredMixin, DeleteView):
    """
    View para a exclusão de veiculos
    """
    model = Veiculo
    template_name = 'veiculo/deletar.html'
    success_url = reverse_lazy('listar-veiculos')

class FotoVeiculo(View):
    """
    View para retornar a foto dos veiculos.
    """

    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}'.format(arquivo))
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            raise Http404("Foto não encontrada ou acesso não-autorizado!")
        except Exception as exception:
            raise exception