from django.shortcuts import render, redirect
from .models import *
import random
from django.http import HttpResponse, JsonResponse
import traceback


def index(request):
    # Aqui você faz referência ao template index.html da pasta Home/templates/Home
    return render(request, 'Home/index.html')


def matematica(request):
    return render(request, 'Home/matematica.html')


def matematica6(request):
    # valor default só pra testar
    category = request.GET.get("category", "Matemática")
    context = {'category': category, 'categories': Category.objects.all()}
    return render(request, 'Home/matematica/6matematica.html', context)


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


def get_quiz(request):
    try:
        category_param = request.GET.get('category')
        question_objs = Question.objects.all()

        if category_param:
            question_objs = question_objs.filter(
                category__category_name__icontains=category_param)

        question_list = list(question_objs)
        data = []
        random.shuffle(question_list)

        for question in question_list:
            data.append({
                "uid": question.uid,
                "category": question.category.category_name,
                "question": question.question,
                "marks": question.marks,
                "answers": question.get_answers()
            })

        payload = {'status': True, 'data': data}
        return JsonResponse(payload)

    except Exception as e:
        import traceback
        return HttpResponse(f"Erro interno: {traceback.format_exc()}")


def quiz(request):
    context = {'category': request.GET.get("category")}
    category = request.GET.get("category")
    return render(request, "quiz.html", {"category": category}, context)
