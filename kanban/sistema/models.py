from django.db import models
from django.utils import timezone

# Create your models here.
class Nivel(models.Model):
    descricao = models.CharField(max_length=200, default="Nível")

    def __str__(self):
        return self.descricao

class Tarefa(models.Model):
    descricao = models.CharField(max_length=200, blank=True)
    titulo = models.CharField(max_length=200, default="Tarefa")
    data = models.DateField(default=timezone.now)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.titulo