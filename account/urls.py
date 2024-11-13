from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import *

app_name = 'user'

urlpatterns = [
    path('login/', views.user_login, name="login"),
]