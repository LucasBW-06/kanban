from django.http import HttpResponse
from .models import Tarefa
from django.shortcuts import render

def index(request):
    tarefas = Tarefa.objects.order_by('id')
    contexto = {'tarefas':tarefas}
    return render(request, 'paginas/index.html', contexto)