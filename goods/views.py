from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template.autoreload import reset_loaders

from goods.models import Categories, Products
# Create your views here.


def catalog(request, category_slug):

    page = request.GET.get("page", 1)

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
    
    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context = {
        "title": "Catalog - Каталог",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context=context)


def product(request, product_slug):
    res = Products.objects.filter(slug=product_slug).first()
    if res:
        context = {
            "product": res,
        }
        return render(request, "goods/product.html", context=context)
