from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    # Aqui você faz referência ao template index.html da pasta Home/templates/Home
    return render(request, 'Home/index.html')


def matematica(request):
    return render(request, 'Home/matematica.html')


def portugues(request):
    return render(request, 'Home/portugues.html')
