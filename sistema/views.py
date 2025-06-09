from django.http import HttpResponse
from .models import Tarefa
from .models import Nivel
from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    tarefas = Tarefa.objects.order_by('titulo')
    niveis = Nivel.objects.order_by('id')
    nivel_min = Nivel.objects.order_by('id').first().id
    nivel_max = Nivel.objects.order_by('-id').first().id
    contexto = {'tarefas':tarefas,
                'niveis':niveis,
                'nivel_min': nivel_min,
                'nivel_max': nivel_max}
    return render(request, 'paginas/index.html', contexto)

def modificiar_nivel(request, id_tarefa, modificador):
    tarefa = get_object_or_404(Tarefa, pk=id_tarefa)
    tarefa.nivel = get_object_or_404(Nivel, id=(tarefa.nivel.id + int(modificador)))
    tarefa.save()

    return redirect('sistema:index')