from django.http import HttpResponse
from django.template import loader

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
        'diarias': [
            {
                "id": 1,
                "dia": "07/11/2023",
                "disponibilidade": "Disponivel",
                "preco": 300
            },
            {
                "id": 2,
                "dia": "08/11/2023",
                "disponibilidade": "Ocupado",
                "preco": 300
            },
        ]
    }
    return HttpResponse(template.render(context, request))

def diaria(request, id):    
    diarias = [
            {
                "id": 1,
                "dia": "07/11/2023",
                "disponibilidade": "Disponivel",
                "preco": 300
            },
            {
                "id": 2,
                "dia": "08/11/2023",
                "disponibilidade": "Ocupado",
                "preco": 300
            },
        ]
    diaria = diarias[id-1]
    template = loader.get_template('diaria.html')
    context = {
        'diaria': diaria,
    }
    return HttpResponse(template.render(context, request))