from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.



def home(request):
    return render(request, 'home/index.html')

def pagina_login(request):
    return render( request, 'home/login.html')

    
def logar(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('home:index')
        else:
            raise 403
    else:
        raise 403