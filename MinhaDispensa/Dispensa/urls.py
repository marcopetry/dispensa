from django.urls import path
from .views import home, itens, lancar_item, alterar_item, delete_item, estoque, estoque_form, alterar_estoque, delete_estoque

urlpatterns = [
    path('', home, name='home'),
    path('itens/', itens, name='itens'),
    path('novo', lancar_item, name='lancar_item'),
    path('alterar_item/<int:id>/', alterar_item, name='alterar_item'),
    path('delete_item/<int:id>/', delete_item, name='delete_item'),

    path('estoque/', estoque, name='estoque'),
    path('lancar/', estoque_form, name='estoque_form'),
    path('alterar_estoque/<int:id>/', alterar_estoque, name='alterar_estoque'),
    path('delete_estoque/<int:id>/', delete_estoque, name='delete_estoque'),
]