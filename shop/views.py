from django.shortcuts import render , get_object_or_404
from .models import Product, Category

# Create your views here.


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products': products,
    }
    request.session['phone'] = '09123456789'
    return render(request, 'shop/product_list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, slug=slug, id=id)
    phone = request.session.get('phone')
    # to delete session
    # del request.session['phone']
    context = {
        'product': product,
        'phone': phone,
    }
    return render(request, 'shop/product_detail.html', context)
