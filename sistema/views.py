from pydoc import describe

from django.http import HttpResponse
from .models import Tarefa
from .models import Nivel
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from django.db import models
from datetime import date

def index(request):
    tarefas = Tarefa.objects.order_by('titulo')
    niveis = Nivel.objects.order_by('indice')
    nivel_max = Nivel.objects.aggregate(models.Max('indice'))['indice__max']
    contexto = {'tarefas':tarefas,
                'niveis':niveis,
                'nivel_max': nivel_max}
    return render(request, 'paginas/index.html', contexto)

def niveis(request):
    niveis = Nivel.objects.order_by('indice')
    nivel_max = Nivel.objects.aggregate(models.Max('indice'))['indice__max']
    contexto = {'niveis': niveis,
                'nivel_max': nivel_max}
    return render(request, 'paginas/niveis.html', contexto)

def tarefa_add(request):
    total = Tarefa.objects.count()
    sugestao = 'Tarefa ' + str(total + 1)
    contexto = {'sugestao': sugestao}

    return render(request, 'paginas/tarefa_add.html', contexto)

def tarefa_edit(request, id_tarefa):
    tarefa = get_object_or_404(Tarefa, pk=id_tarefa)
    contexto = {'tarefa': tarefa}

    return render(request, 'paginas/tarefa_edit.html', contexto)

def modificar_nivel(request, id_tarefa, modificador):
    tarefa = get_object_or_404(Tarefa, pk=id_tarefa)
    tarefa.nivel += int(modificador)
    tarefa.save()

    return redirect('sistema:index')

def modificar_indice(request, indice_nivel, modificador):
    modificador = int(modificador)
    tarefas = Tarefa.objects.all()
    nivel = get_object_or_404(Nivel, indice=indice_nivel)
    nivel_ = get_object_or_404(Nivel, indice=(indice_nivel+modificador))

    nivel.indice += modificador
    nivel_.indice += -modificador

    nivel.save()
    nivel_.save()

    for tarefa in tarefas:
        if tarefa.nivel == indice_nivel:
            tarefa.nivel += modificador
        elif tarefa.nivel == indice_nivel+modificador:
            tarefa.nivel += -modificador
        tarefa.save()

    return redirect('sistema:niveis')

def deletar_nivel(request, id_nivel):
    Nivel.objects.filter(indice=id_nivel).delete()
    Nivel.objects.filter(indice__gt=id_nivel).update(indice=F('indice') - 1)
    Tarefa.objects.filter(nivel=id_nivel).delete()
    Tarefa.objects.filter(nivel__gt=id_nivel).update(nivel=F('nivel') - 1)

    return redirect('sistema:niveis')

def deletar_tarefa(request,id_tarefa):
    Tarefa.objects.filter(id=id_tarefa).delete()
    return redirect('sistema:index')

def adicionar_nivel(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        novo_nivel = Nivel(descricao=descricao)
        novo_nivel.save()

    return redirect('sistema:niveis')

def adicionar_tarefa(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')

        data = request.POST.get('data')
        prazo = None
        if data:
            prazo = date.fromisoformat(data)

        nova_tarefa = Tarefa(titulo=titulo,
                             descricao=descricao,
                             data=prazo)
        nova_tarefa.save()

    return redirect('sistema:index')

def editar_tarefa(request, id_tarefa):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')

        data = request.POST.get('data')
        prazo = None
        if data:
            prazo = date.fromisoformat(data)

        tarefa = get_object_or_404(Tarefa, pk=id_tarefa)

        tarefa.titulo = titulo
        tarefa.descricao = descricao
        tarefa.data = prazo

        tarefa.save()

    return redirect('sistema:index')
