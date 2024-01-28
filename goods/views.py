from django.shortcuts import render
from django.template.autoreload import reset_loaders

from goods.models import Categories, Products
# Create your views here.


def catalog(request):

    goods = Products.objects.all()
    
    context = {
        "title": "Catalog - Каталог",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context=context)


def product(request, product_slug):
    res = Products.objects.filter(slug=product_slug).first()
    if res:
        context = {
            "product": res,
        }
        return render(request, "goods/product.html", context=context)
