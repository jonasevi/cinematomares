from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    # Vista de Películas
    path('', views.peliculas_list, name='peliculas_list')
]