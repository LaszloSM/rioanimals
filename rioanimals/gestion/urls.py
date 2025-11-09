from django.urls import path
from . import views

app_name = 'gestion'

urlpatterns = [
    path('', views.lista_animales, name='lista_animales'),
    path('animal/<int:animal_id>/', views.detalle_animal, name='detalle_animal'),
    path('adoptantes/', views.lista_adoptantes, name='lista_adoptantes'),
    path('voluntarios/', views.lista_voluntarios, name='lista_voluntarios'),
    path('adopciones/', views.lista_adopciones, name='lista_adopciones'),
]
