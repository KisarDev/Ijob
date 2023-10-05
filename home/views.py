from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse, HttpResponseServerError
from django.http import request
from django.contrib.auth.hashers import make_password
from django.contrib import messages
import time



from home.forms import UserForm
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
        login(request, user)
        return redirect('home:index')
    else:
        print("não ativa")
        raise 403
    

def registrar(request):
    register_form_data = request.session.get('register_form_data', None)
    form= UserForm(register_form_data)
    return render(request, "home/criar_conta.html", {"form": form})

def criar(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = UserForm(POST)

    if form.is_valid():
        form.save()
        del(request.session['register_form_data'])
        return redirect('home:login')
    else:
        messages.error(request, "Erro nos campos")    

    # Redirecione para a página de registro após processar o formulário,
    # independente de ser válido ou não.
    return redirect('home:registrar')

    
