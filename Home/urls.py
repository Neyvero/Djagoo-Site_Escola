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
    # Rota para a página de Português
    path('portugues/', views.portugues, name='portugues'),
]
