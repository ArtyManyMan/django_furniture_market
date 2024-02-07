from django.urls import path

from orders import views as views_orders

app_name = "orders"

urlpatterns = [
    path('create-order/', views_orders.create_order, name="create_order"),
]
