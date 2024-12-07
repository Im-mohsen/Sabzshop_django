from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('products/', views.ProductListApiView.as_view(), name='products_list_api'),
    path('product/<int:pk>/', views.ProductDetailApiView.as_view(), name='product_detail_api'),
]
