from django.urls import path
from . import views

app_name = 'sistema'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id_tarefa>/modificar_nivel/<str:modificador>', views.modificiar_nivel, name='modificar_nivel'),
    path('<int:id_tarefa>/deletar_tarefa', views.deletar_tarefa, name='deletar_tarefa'),
    path('<int:id_nivel>/deletar_nivel', views.deletar_nivel, name='deletar_nivel')
]