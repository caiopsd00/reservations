from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('app/reservas/', views.produzindo, name='produzindo'),
    path('app/administrador/', views.administrador, name='administrador'),
    path('app/administrador/diaria/<int:id>', views.diaria, name='diaria'),
    path('app/administrador/diaria/criar', views.diariaCriar, name='diariaCriar'),
    path('app/administrador/descricao/<int:id>', views.descricao, name='descricao'),
    path('app/administrador/descricao/criar', views.descricaoCriar, name='descricaoCriar'),
    path('auth/login/', views.produzindo, name='produzindo'),
    path('auth/cadastro/', views.produzindo, name='produzindo'),
]