from django.urls import path
from carts import views as views_carts


app_name = "carts"

urlpatterns = [
    path('cart_add/<int:product_id>', views_carts.cart_add, name="cart_add"),
    path('cart_change/<int:product_id>', views_carts.cart_change, name="cart_change"),
    path('cart_remove/<int:product_id>', views_carts.cart_remove, name="cart_remove"),
]