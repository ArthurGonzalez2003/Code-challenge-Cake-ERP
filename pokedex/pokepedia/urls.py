from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pokedex'),
    path('<slug:pkm>', views.pokemon_data, name='pokemon-page'),
    path('hd/<slug:pkm>', views.pokemon_data_hd, name='pokemon-page'),
]
