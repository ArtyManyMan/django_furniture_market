from django.urls import path
from goods import views as views_goods

app_name = "goods"

urlpatterns = [
    path("", views_goods.catalog, name="index"),
    path("product/", views_goods.product, name="product"),
]