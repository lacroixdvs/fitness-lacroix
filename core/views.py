from django.shortcuts import render

def bienvenida(request):
    return render(request, 'core/bienvenida.html')