from django.contrib import admin
from anuncio.models import Anuncio

class AnuncioAdmin(admin.ModelAdmin):
    list_display = ['id', 'data', 'descricao', 'preco', 'veiculo', 'usuario']
    search_fields = ['modelo']

admin.site.register(Anuncio, AnuncioAdmin)
