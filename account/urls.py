from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import *

app_name = 'user'

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('logout/', views.log_out, name='logout'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit_user, name='edit_user'),

]