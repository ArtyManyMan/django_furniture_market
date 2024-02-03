from django.urls import path
from carts import views as views_carts


app_name = "carts"

urlpatterns = [
    path('cart_add/<slug:product_slug>', views_carts.cart_add, name="cart_add"),
    path('cart_change/<slug:produc_tslug>', views_carts.cart_change, name="cart_change"),
    path('cart_remove/<slug:product_slug>', views_carts.cart_remove, name="cart_remove"),
]