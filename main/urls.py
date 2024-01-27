from django.urls import path
from . import views as views_main

app_name = "main"

urlpatterns = [
    path("", views_main.index, name="index"),
    path("about/", views_main.about, name="about"),
]