from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from .models import ProductInfo

def get_product_context(_request):
    product_list = ProductInfo.objects.all()
    product_dict = []
    for product in product_list:
        product_dict.append(product.dict())
    return RequestContext(_request, {
        'product_list': product_list,
		'product_dict': product_dict,
    })

def index(request):
    return render(request, 'register/index.html', get_product_context(request))

def detail(request, product_id):
    return render(request, 'register/detail.html',
        {'product': get_object_or_404(ProductInfo, pk=product_id)})

def cart(request):
    return render(request, 'register/cart.html', get_product_context(request))
