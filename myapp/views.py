from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Diaria
from .models import Descricoes

def produzindo(request):
    template = loader.get_template('produzindo.html')
    context = {
        "nome": "Domo Recanto X",
        "cidade": "Cunha"
    }
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('home.html')
    context = {
        "nome": "Domo Recanto X",
        "cidade": "Cunha"
    }
    return HttpResponse(template.render(context, request))

def administrador(request):
    template = loader.get_template('administrador.html')
    context = {
        'diarias': Diaria.objects.all().values(),
        'descricoes': Descricoes.objects.all().values()
    }
    return HttpResponse(template.render(context, request))

def diaria(request, id):    
    diaria = Diaria.objects.get(id=id)
    template = loader.get_template('diaria.html')
    context = {
        'diaria': diaria,
    }
    return HttpResponse(template.render(context, request))

def diariaCriar(request):    
    return render(request, 'diariaCriar.html')

    
def descricao(request, id):    
    descricoes = Descricoes.objects.get(id=id)
    template = loader.get_template('descricoes.html')
    context = {
        'descricoes': descricoes,
    }
    return HttpResponse(template.render(context, request))

def descricaoCriar(request):    
    return render(request, 'descricaoCriar.html')