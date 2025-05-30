from django.db import models

# Create your models here.
class Status(models.Model):
    descricao = models.CharField(max_length=200)

class Tarefa(models.Model):
    descricao = models.CharField(max_length=200)
    Status = models.IntegerField(default=0)