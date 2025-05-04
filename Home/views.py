from django.shortcuts import render
from .models import *
import random
from django.http import HttpResponse, JsonResponse


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

# {
#   'status' : True
#    'data' : [
#        {
#            },
#    ]
# }


def get_quiz(request):
    try:
        question_objs = list(Question.objects.all())
        data = []
        random.shuffle(question_objs)

        for question_objs in question_objs:

            data.append({
                "category": question_objs.category.category_name,
                "question": question_objs.question,
                "marks": question_objs.marks,
                "answers": question_objs.get_answers()
            })

        payload = {'status': True, 'data': data}

        return JsonResponse(payload)

    except Exception as e:
        print(e)
    return HttpResponse("Somethig went Wrong")
