from django import forms
from .models import Item, Estoque

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = {'nome', 'unidade_medida', 'categoria', 'valor_unitario', 'quantidade_minima_desejada'}

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = {'data_entrada', 'ultima_data_saida', 'quantidade', 'item', 'valor_total'}