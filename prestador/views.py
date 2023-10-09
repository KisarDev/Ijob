from django.shortcuts import render
from .models import Profissao
from django.contrib import messages
from core.settings import constants
# Create your views here.

def cadastrar_profissao(request):
    if request.method == 'POST':
        profissao = request.POST.get('profissao')
        tempo = request.POST.get('tempo')
        preco = request.POST.get('preco')
        foto = request.FILES.get('foto')

        if not profissao or not tempo or not preco or not foto:
            messages.error(request, 'Por favor, preencha todos os campos do formulário.')
        else:
            nova_profissao = Profissao(profissao=profissao,tempo_experiencia=tempo,preco_por_hora=preco,foto=foto)
            nova_profissao.save()

            messages.add_message(request, constants.SUCCESS, 'Profissão cadastrada com sucesso!')
            return render(request, 'cadastro.html', {'nova_profissao':nova_profissao})
    
    return render(request, 'cadastro.html')
    