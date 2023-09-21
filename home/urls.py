from django.contrib import admin
from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home),
    path('login/', views.login, name='login'),
]
