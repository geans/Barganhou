from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import ProductInfo

def index (request):
    latest_product_list = ProductInfo.objects.order_by('-date_log')[:5]
    template = loader.get_template('register/index.html')
    context = RequestContext(request, {
        'latest_product_list': latest_product_list,
    })
    return render(request, 'polls/index.html', context)

def detail (request, product_id):
    return HttpResponse("Você está vendo detalhes do produto %s." % product_id)

def price (request, product_id):
    return HttpResponse("Você está vendo o preço do produto %s." % product_id)
    
def local (request, product_id):
    return HttpResponse("Você está vendo o local de registro do produto %s." % product_id)
