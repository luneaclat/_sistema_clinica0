from django.shortcuts import render

# Aqui fica a primeira view
def index(request):
    return render(
    request,
    'global/base.html',
    )

def seunome(request):
    return render(
    request,
    'global/seunome.html',
    )
# REQUEST E RESPONSE E RENDER