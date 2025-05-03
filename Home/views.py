from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    # Aqui você faz referência ao template index.html da pasta Home/templates/Home
    return render(request, 'Home/index.html')


def matematica(request):
    return render(request, 'Home/matematica.html')


def matematica6(request):
    return render(request, 'Home/matematica/6matematica.html')


def matematica7(request):
    return render(request, 'Home/matematica/7matematica.html')


def matematica8(request):
    return render(request, 'Home/matematica/8matematica.html')


def matematica9(request):
    return render(request, 'Home/matematica/9matematica.html')


def portugues(request):
    return render(request, 'Home/portugues.html')


def portugues6(request):
    return render(request, 'Home/portugues/6portugues.html')


def portugues7(request):
    return render(request, 'Home/portugues/7portugues.html')


def portugues8(request):
    return render(request, 'Home/portugues/8portugues.html')


def portugues9(request):
    return render(request, 'Home/portugues/9portugues.html')
