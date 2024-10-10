from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from anuncio.models import Anuncio
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from anuncio.form import FormularioAnuncio

class ListarAnuncios(LoginRequiredMixin, ListView):
    """
    View para listar os anuncios cadastrados.
    """
    model = Anuncio
    context_object_name = 'anuncios'
    template_name = 'anuncio/listarA.html'

class CriarAnuncios(LoginRequiredMixin, CreateView):
    """
    View para criar os anuncios de veiculos.
    """
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/novoA.html'
    success_url = reverse_lazy('listar-anuncios')

class EditarAnuncios(LoginRequiredMixin, UpdateView):
    """
    View para a edição de anuncios já cadastrados
    """
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/editarA.html'
    success_url = reverse_lazy('listar-anuncios')

class DeletarAnuncios(LoginRequiredMixin, DeleteView):
    """
    View para a exclusão de anuncios
    """
    model = Anuncio
    template_name = 'anuncio/deletarA.html'
    success_url = reverse_lazy('listar-anuncios')

class FotoAnuncio(View):
    """
    View para retornar a foto dos anuncios.
    """

    def get(self, request, arquivo):
        try:
            anuncio = Anuncio.objects.get(foto='anuncio/fotos/{}'.format(arquivo))
            return FileResponse(anuncio.foto)
        except ObjectDoesNotExist:
            raise Http404("Foto não encontrada ou acesso não-autorizado!")
        except Exception as exception:
            raise exception