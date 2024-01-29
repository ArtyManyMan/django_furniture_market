from django.urls import path
from goods import views as views_goods

from django.db.models import Q

app_name = "goods"

urlpatterns = [
    path('search/', views_goods.catalog, name="search"),
    path("<slug:category_slug>/", views_goods.catalog, name="index"),
    path("product/<slug:product_slug>/", views_goods.product, name="product"),
]