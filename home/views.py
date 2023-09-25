from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.



def home(request):
    return render(request, 'home/index.html')

def pagina_login(request):
    return render( request, 'home/login.html')

    
class Login(View):
    def logar(self, request):
        if request.method == "POST":
            username = self.request.POST.get("username")
            password = self.request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if not user:
                raise 404  # Redireciona para a página inicial após o login bem-sucedido

        # Se o login falhar, você pode adicionar uma mensagem de erro ao contexto
        context = {
            'error_message': 'Nome de usuário ou senha incorretos.'  # Mensagem de erro de exemplo
        }
        return print("não existe")