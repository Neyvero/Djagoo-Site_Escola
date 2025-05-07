from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]

app_name = "Home"
urlpatterns = [
    path("", views.index, name="index"),
    # Rota para a página de Matemática
    path('matematica/', views.matematica, name='matematica'),
    path('matematica/6matematica/', views.matematica6, name='6matematica'),
    path('matematica/7matematica/', views.matematica7, name='7matematica'),
    path('matematica/8matematica/', views.matematica8, name='8matematica'),
    path('matematica/9matematica/', views.matematica9, name='9matematica'),
    # Rota para a página de Português
    path('portugues/', views.portugues, name='portugues'),
    path('portugues/6portugues', views.portugues6, name='6portugues'),
    path('portugues/7portugues', views.portugues7, name='7portugues'),
    path('portugues/8portugues', views.portugues8, name='8portugues'),
    path('portugues/9portugues', views.portugues9, name='9portugues'),
    # Rota para a página de Geografia
    path('geografia/', views.geografia, name='geografia'),
    path('geografia/6geografia', views.geografia6, name='6geografia'),
    path('geografia/7geografia', views.geografia7, name='7geografia'),
    path('geografia/8geografia', views.geografia8, name='8geografia'),
    path('geografia/9geografia', views.geografia9, name='9geografia'),
    # Rota para a página de História
    path('historia/', views.historia, name='historia'),
    path('historia/6historia', views.historia6, name='6historia'),
    path('historia/7historia', views.historia7, name='7historia'),
    path('historia/8historia', views.historia8, name='8historia'),
    path('historia/9historia', views.historia9, name='9historia'),
    # Rota para os quizes
    path('api/get-quiz/', views.get_quiz, name="get_quiz"),

]
