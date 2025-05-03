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
]
