from django.shortcuts import render, redirect, get_object_or_404
from .models import Venda
from .forms import VendaForm

def lista_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'vendas/lista.html', {'vendas': vendas})


def criar_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vendas')
    else:
        form = VendaForm()
    return render(request, 'vendas/form.html', {'form': form, 'acao': 'Adicionar'})


def editar_venda(request, id):
    venda = get_object_or_404(Venda, id=id)
    if request.method == 'POST':
        form = VendaForm(request.POST, instance=venda)
        if form.is_valid():
            form.save()
            return redirect('lista_vendas')
    else:
        form = VendaForm(instance=venda)
    return render(request, 'vendas/form.html', {'form': form, 'acao': 'Editar'})


def excluir_venda(request, id):
    venda = get_object_or_404(Venda, id=id)
    if request.method == 'POST':
        venda.delete()
        return redirect('lista_vendas')
    return render(request, 'vendas/confirmar_exclusao.html', {'venda': venda})
