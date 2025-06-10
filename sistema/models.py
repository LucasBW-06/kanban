from django.db import models
from django.utils import timezone

class Nivel(models.Model):
    descricao = models.CharField(max_length=200, blank=True, null=True)
    indice = models.PositiveIntegerField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.indice:
            self.indice = (Nivel.objects.aggregate(models.Max('indice'))['indice__max'] or 0) + 1
        if not self.descricao:
            self.descricao = 'Nível ' + str(self.indice)
            
        super().save(*args, **kwargs)

    def __str__(self):
        return self.descricao

class Tarefa(models.Model):
    descricao = models.CharField(max_length=200, blank=True)
    titulo = models.CharField(max_length=200, blank=True, null=True)
    data = models.DateField(default=timezone.now)
    nivel = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        if not self.titulo:
            self.titulo = 'Tarefa ' + str(Tarefa.objects.count() + 1)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    def nivel_obj(self):
        return Nivel.objects.filter(indice=self.nivel).first()