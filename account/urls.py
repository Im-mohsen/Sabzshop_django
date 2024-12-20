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
    path('password_change/', views.password_change, name='password_change'),
    path('password_change/done/', views.password_change_done, name='password_change_done'),
    path('add_address/', views.add_address, name='add_address'),
    path('add_address/done/', views.add_address_done,name='add_address_done'),
]
