from django.forms import ModelForm
from anuncio.models import Anuncio

class FormularioAnuncio(ModelForm):
    """
    formulario para o model Anuncio
    """

    class Meta:
        model = Anuncio
        exclude = []