from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('products/', views.product_list, name='products_list'),
    path('products/<slug:category_slug>/', views.product_list, name='products_list_by_category'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
