from django.urls import include, path
from users import views as views_users

app_name = 'users'

urlpatterns = [
    path("login/", views_users.login, name='login'),
    path("registration/", views_users.registration, name='registration'),
    path("profile/", views_users.profile, name='profile'),
    path("logout/", views_users.logout, name='logout')
]