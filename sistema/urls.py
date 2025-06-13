from django.urls import path
from . import views

app_name = 'sistema'

urlpatterns = [
    path('', views.index, name="index"),
    path('niveis/', views.niveis, name="niveis"),
    path('niveis/adicionar/', views.add_niveis, name="adicionar_nivel"),
    path('modificar_nivel/<int:id_tarefa>/<str:modificador>', views.modificar_nivel, name='modificar_nivel'),
    path('modificar_indice/<int:indice_nivel>/<str:modificador>', views.modificar_indice, name='modificar_indice'),
    path('deletar_tarefa/<int:id_tarefa>', views.deletar_tarefa, name='deletar_tarefa'),
    path('deletar_nivel/<int:id_nivel>', views.deletar_nivel, name='deletar_nivel'),
    path('adicionar_nivel/', views.adicionar_nivel, name='adicionar_nivel')
]