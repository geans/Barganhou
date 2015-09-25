from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from .models import ProductInfo, LocalInfo

def get_product_context(request):
    products = []
    locals = []
    for product in ProductInfo.objects.all():
        products.append(product.dict())
    for local in LocalInfo.objects.all():
        locals.append(local.dict())
    return RequestContext(request, {
		'products': products,
        'locals': LocalInfo.objects.all(),
    })

def index(request):
    return render(request, 'register/index.html', get_product_context(request))

def cart(request):
    return render(request, 'register/cart.html', get_product_context(request))

def detail(request, product_id):
    return render(request, 'register/detail.html',
        {'product': get_object_or_404(ProductInfo, pk=product_id)})

def local(request, local_id):
    return render(request, 'register/local.html',
        {'local': get_object_or_404(LocalInfo, pk=local_id)})
