from django.contrib import admin
from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='index'),
    path('login/', views.pagina_login, name='login'),
    path('logar/', views.Login.as_view(), name="logar")
]
