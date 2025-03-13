# SÃO AS IMPORTAÇÕES REALIZADAS DE FORMA A UTILIZAR PARTES DO DJANGO.
from django.contrib import admin
from django.urls import path, include

# lISTA RESPONSÁVEL POR ORGANIZAR AS URLS DO SISTEMA.
urlpatterns = [
    path('', include('sistema.urls')),
    path('admin/', admin.site.urls),
]

# path() -> é um método do django que permite realizar a inserção de urls.
