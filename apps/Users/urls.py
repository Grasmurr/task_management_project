from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("registration/", views.registration_view, name='registration'),
    path("login/", views.login_view, name='login')
]