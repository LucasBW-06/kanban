from django.http import HttpResponse
from .models import Tarefa
from .models import Nivel
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F
from django.db import models

def index(request):
    tarefas = Tarefa.objects.order_by('titulo')
    niveis = Nivel.objects.order_by('indice')
    nivel_min = 1
    nivel_max = Nivel.objects.aggregate(models.Max('indice'))['indice__max']
    contexto = {'tarefas':tarefas,
                'niveis':niveis,
                'nivel_min': nivel_min,
                'nivel_max': nivel_max}
    return render(request, 'paginas/index.html', contexto)

def modificiar_nivel(request, id_tarefa, modificador):
    tarefa = get_object_or_404(Tarefa, pk=id_tarefa)
    tarefa.nivel += int(modificador)
    tarefa.save()

    return redirect('sistema:index')

def modificar_indice(request, indice_nivel, modificador):
    modificador = int(modificador)
    tarefas = Tarefa.objects
    nivel = get_object_or_404(Nivel, indice=indice_nivel)
    nivel_ = get_object_or_404(Nivel, indice=indice_nivel+modificador)

    nivel.indice += modificador
    nivel_.indice += -modificador

    for tarefa in tarefas:
        if tarefa.nivel == indice_nivel:
            tarefa.nivel += modificador
        elif tarefa.nivel == indice_nivel+modificador:
            tarefa.nivel += -modificador
        tarefa.save()

def deletar_nivel(request, id_nivel):
    Nivel.objects.filter(indice=id_nivel).delete()
    Nivel.objects.filter(indice__gt=id_nivel).update(F('indice') - 1)
    Tarefa.objects.filter(nivel=id_nivel).delete()
    Tarefa.objects.filter(nivel__gt=id_nivel).update(F('nivel') - 1)

def deletar_tarefa(request,id_tarefa):
    Tarefa.objects.filter(id=id_tarefa).delete()
    return redirect('sistema:index')