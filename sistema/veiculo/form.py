from django.forms import ModelForm
from veiculo.models import Veiculo

class FormularioVeiculo(ModelForm):
    """
    formulario para o model Veiculo
    """

    class Meta:
        model = Veiculo
        exclude = []