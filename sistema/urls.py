from django.urls import path
from . import views

app_name = 'sistema'

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id_tarefa>/modificar_nivel/<str:modificador>', views.modificiar_nivel, name='modificar_nivel'),
]