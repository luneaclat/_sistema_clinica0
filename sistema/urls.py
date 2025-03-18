# SÃO AS IMPORTAÇÕES REALIZADAS DE FORMA A UTILIZAR PARTES DO DJANGO.
from django.urls import path
# IMPORTAÇÃO DO MÓDULO VIEWS.PY, ONDE TEM A VIEW INDEX.
from sistema import views

app_name = 'sistema'

# lISTA RESPONSÁVEL POR ORGANIZAR AS URLS DO SISTEMA.
urlpatterns = [
    path('', views.index, name='index'),
    path('seunome/', views.seunome, name='nome'),
]
