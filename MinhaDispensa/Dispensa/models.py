import uuid
from django.db import models

# Create your models here.
tipos_categorias = (
        ('Limpeza', 'Limpeza'),
        ('Alimentação', 'Alimentação'),
        ('Higiene Pessoal', 'Higiene Pessoal'),
        ('Outro', 'Outro'),
    )

medidas = (
    ('Un', 'Unidades'),
    ('Pct', 'Pacotes'),
    ('Kg', 'Peso'),
)

class Item(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=30, choices=tipos_categorias)
    unidade_medida = models.CharField(max_length=10, choices=medidas)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_minima_desejada = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Estoque(models.Model):
    data_entrada = models.DateField()
    ultima_data_saida = models.DateField(null=True, blank=True)
    quantidade = models.DecimalField(max_digits=10, decimal_places=3)
    item = models.ManyToManyField("Item")
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self

class Morador(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    senha = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

#Item, Morador, Estoque