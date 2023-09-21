from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
# Create your views here.



def home(request):
    return render(request, 'home/index.html')

def pagina_login(request):
    return render( request, 'home/login.html')

    
class Login(View):
    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        if not username or not password:
            pass
        usuario = authenticate(self.request, username=username, password=password)
        login = login(self.request, user=usuario)
        return redirect(
            'home/index.html'
        )