# SÃO AS IMPORTAÇÕES REALIZADAS DE FORMA A UTILIZAR PARTES DO DJANGO.
from django.contrib import admin
from django.urls import path

# lISTA RESPONSÁVEL POR ORGANIZAR AS URLS DO SISTEMA.
urlpatterns = [
    path('admin/', admin.site.urls),
]

# path() -> é um método do django que permite realizar a inserção de urls.
