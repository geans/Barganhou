from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
    return HttpResponse("Ôpa! Estás na primeira página do Registro de Informações de Produtos")

def detail (request, product_id):
    return HttpResponse("Você está vendo detalhes do produto %s." % product_id)
