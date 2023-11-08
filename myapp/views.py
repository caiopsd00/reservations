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

def cadastroDescricao(request):
    if request.method == "GET":
        return render(request, 'descricaoCriar.html')
    else:
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')

        descricoes = Descricoes.objects.filter(titulo=titulo).first()
        if descricoes:
            return HttpResponse('Já uma descrição com esse título')

        novaDescricao = Descricoes()

        novaDescricao.titulo=titulo 
        novaDescricao.descricao=descricao

        novaDescricao.save()

        template = loader.get_template('administrador.html')
        context = {
            'diarias': Diaria.objects.all().values(),
            'descricoes': Descricoes.objects.all().values()
        }
        return HttpResponse(template.render(context, request))

def cadastroDiaria(request):
    if request.method == "GET":
        return render(request, 'diariaCriar.html')
    else:
        dia = request.POST.get('dia')
        disponibilidade = request.POST.get('disponibilidade')
        preco = request.POST.get('preco')

        diaria = Diaria.objects.filter(dia=dia).first()
        if diaria:
            return HttpResponse('Diaria ja cadastrada')

        novaDiaria = Diaria()
        
        novaDiaria.dia = dia
        novaDiaria.disponibilidade = disponibilidade == 'on'
        novaDiaria.preco = preco

        novaDiaria.save()

        template = loader.get_template('administrador.html')
        context = {
            'diarias': Diaria.objects.all().values(),
            'descricoes': Descricoes.objects.all().values()
        }
        return HttpResponse(template.render(context, request))


def atualizacaoDiaria(request):
    if request.method == "GET":
        template = loader.get_template('administrador.html')
        context = {
            'diarias': Diaria.objects.all().values(),
            'descricoes': Descricoes.objects.all().values()
        }
        return HttpResponse(template.render(context, request))
    else:
        id = request.POST.get('id')
        dia = request.POST.get('dia')
        disponibilidade = request.POST.get('disponibilidade')
        preco = request.POST.get('preco')
        diaria_existente = Diaria.objects.filter(id=id).first()

        if diaria_existente:
            diaria_existente.dia = dia
            diaria_existente.disponibilidade = disponibilidade == 'on'
            diaria_existente.preco = preco

            diaria_existente.save()

            template = loader.get_template('administrador.html')
            context = {
                'diarias': Diaria.objects.all().values(),
                'descricoes': Descricoes.objects.all().values()
            }
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponse('Diaria não existe')


def atualizacaoDescricao(request):
    if request.method == "GET":
        template = loader.get_template('administrador.html')
        context = {
            'diarias': Diaria.objects.all().values(),
            'descricoes': Descricoes.objects.all().values()
        }
        return HttpResponse(template.render(context, request))
    else:
        id = request.POST.get('id')
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        descricao_existente = Descricoes.objects.filter(id=id).first()

        if descricao_existente:

            descricao_existente.titulo = titulo
            descricao_existente.descricao = descricao

            descricao_existente.save()

            template = loader.get_template('administrador.html')
            context = {
                'diarias': Diaria.objects.all().values(),
                'descricoes': Descricoes.objects.all().values()
            }
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponse('Descrição não existe')