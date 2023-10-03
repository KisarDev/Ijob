from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseServerError
from django.http import request
from django.contrib.auth.hashers import make_password



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
    context ={}
    context['form']= UserForm(register_form_data)
    return render(request, "home/criar_conta.html", context)

def criar(request):
    if request.method != 'POST':
        raise HttpResponseServerError({'error_message': 'Método não permitido'})

    POST = request.POST
    request.session['register_form_data'] = POST
    form = UserForm(POST)

    try:
        if form.is_valid():
            form.save()
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
    
    return redirect("home:login")
