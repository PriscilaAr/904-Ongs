from django.shortcuts import render
from website.models import Pessoa, Ong

# Create your views here.

def index(request):

    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.data_de_nasc = request.POST.get('data_de_nasc')
        pessoa.email = request.POST.get('email')
        pessoa.str_cep = request.POST.get('str_cep')
        pessoa.str_numero = request.POST.get('str_numero')
        pessoa.complemento = request.POST.get('complemento')
        pessoa.genero = request.POST.get('genero')
        pessoa.telefone = request.POST.get('telefone')
        pessoa.celular = request.POST.get('celular')
        pessoa.motivo = request.POST.get('motivo')
        pessoa.save()

        contexto = {
            'nome': pessoa.nome
        }
        return render(request, 'index.html', contexto)


    return render(request, 'index.html')

def pessoas(request):
    pessoas = Pessoa.objects.filter(ativo=True).all()

    contexto = {
        'pessoas': pessoas
    }
    return render(request, 'pessoas.html', contexto) 




def ongs(request):
    if request.method == 'POST':
        ong = Ongs()
        ong.nome = request.POST.get('nome')
        ong.email = request.POST.get('email')
        ong.str_cep = request.POST.get('str_cep')
        ong.str_numero = request.POST.get('str_numero')
        ong.telefone = request.POST.get('telefone')
        ong.observacao = request.POST.get('observacao')
        ong.save()

        contexto = {
            'nome': ong.nome
        }
        return render(request, 'ongs.html', contexto)


    return render(request, 'ongs.html')

def ongs(request):
    ongs = ong.objects.filter(request).all()

    contexto = {
        'ongs': ong
    }
    return render(request, 'ongs.html', contexto) 
