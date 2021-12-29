from django.shortcuts import render, get_object_or_404
from .models import Pelicula


def peliculas_list(request):
    peliculas = Pelicula.objects.filter(estado="published")
    return render(request,
                  'cartelera.html',
                  {'peliculas': peliculas})