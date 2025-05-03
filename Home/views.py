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


def historia(request):
    return render(request, 'Home/historia.html')


def historia6(request):
    return render(request, 'Home/historia/6historia.html')


def historia7(request):
    return render(request, 'Home/historia/7historia.html')


def historia8(request):
    return render(request, 'Home/historia/8historia.html')


def historia9(request):
    return render(request, 'Home/historia/9historia.html')


def geografia(request):
    return render(request, 'Home/geografia.html')


def geografia6(request):
    return render(request, 'Home/geografia/6geografia.html')


def geografia7(request):
    return render(request, 'Home/geografia/7geografia.html')


def geografia8(request):
    return render(request, 'Home/geografia/8geografia.html')


def geografia9(request):
    return render(request, 'Home/geografia/9geografia.html')
