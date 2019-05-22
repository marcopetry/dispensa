from django.shortcuts import render, redirect
from .models import Item, Estoque, Morador
from .forms import ItemForm, EstoqueForm, MoradorForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def itens(request):
    itens = Item.objects.all()
    return render(request, 'itens.html', {'itens': itens})

#Essa view vai lançar um item no estoque
def lancar_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('itens')

    return render(request, 'item_form.html', {'form': form})

def alterar_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('itens')

    return render(request, 'item_form.html', {'form': form, 'item': item})

def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('itens')

    return render(request, 'delete_item.html', {'item': item})

#Esssa view vai retornar uma consulta ao estoque
def estoque(request):
    estoque = Estoque.objects.all()

    return render(request, 'estoque.html', {'estoque': estoque})

def estoque_form(request):
    form = EstoqueForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('estoque')

    return render(request, 'estoque_form.html', {'form': form})

def alterar_estoque(request, id):
    estoque = Estoque.objects.get(id=id)
    form = EstoqueForm(request.POST or None, instance=estoque)
    if form.is_valid():
        form.save()
        return redirect('estoque')

    return render(request, 'estoque_form.html', {'form': form, 'estoque': estoque})

def delete_estoque(request, id):
    estoque = Estoque.objects.get(id=id)

    if request.method == 'POST':
        estoque.delete()
        return redirect('estoque')

    return render(request, 'delete_estoque.html', {'estoque': estoque})

def morador_form(request):
    form = MoradorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('estoque')

    return render(request, 'morador_form.html', {'form': form})

def moradores(request):
    morador = Morador.objects.all()
    return render(request, 'moradores.html', {'morador': morador})

def alterar_dados(request, id):
    morador = Morador.objects.get(id=id)
    form = MoradorForm(request.POST or None, instance=morador)
    if form.is_valid():
        form.save()
        return redirect('moradores')

    return render(request, 'morador_form.html', {'form': form, 'morador': morador})

def delete_morador(request, id):
    morador = Morador.objects.get(id=id)

    if request.method == 'POST':
        morador.delete()
        return redirect('moradores')

    return render(request, 'delete_morador.html', {'morador': morador})