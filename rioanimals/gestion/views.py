from django.shortcuts import render
from .models import TblAnimal, TblAdoptante, TblVoluntario, TblAdopcion


def lista_animales(request):
    animales = TblAnimal.objects.all()
    return render(request, 'gestion/lista_animales.html', {'animales': animales})


def detalle_animal(request, animal_id):
    animal = TblAnimal.objects.get(anim_id=animal_id)
    historial = animal.tblhistorialmedico_set.all()
    return render(request, 'gestion/detalle_animal.html', {
        'animal': animal,
        'historial': historial
    })


def lista_adoptantes(request):
    adoptantes = TblAdoptante.objects.all()
    return render(request, 'gestion/lista_adoptantes.html', {'adoptantes': adoptantes})


def lista_voluntarios(request):
    voluntarios = TblVoluntario.objects.all()
    return render(request, 'gestion/lista_voluntarios.html', {'voluntarios': voluntarios})


def lista_adopciones(request):
    adopciones = TblAdopcion.objects.all()
    return render(request, 'gestion/lista_adopciones.html', {'adopciones': adopciones})
