from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from .models import ProductInfo

def index (request):
    product_list = ProductInfo.objects.all()
    template = loader.get_template('register/index.html')
    product_dict = []
    for product in product_list:
        product_dict.append(product.dict())
    
    context = RequestContext(request, {
        'product_list': product_list,
		'product_dict': product_dict,
    })
    return render(request, 'register/index.html', context)

def detail (request, product_id):
    product = get_object_or_404(ProductInfo, pk=product_id)
    return render(request, 'register/detail.html',
        {'product': product})
