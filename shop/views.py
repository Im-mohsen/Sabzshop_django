from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def product_list(request, category_slug=None):
    products = Product.objects.all()

    # category
    category = None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    products = products
    sort = request.GET.get('sort')  # Default to newest
    valid_sort_fields = ['-created', 'created', 'new_price', '-new_price']

    if sort in valid_sort_fields:
        products = products.order_by(sort)
    else:
        products = products.order_by('-created')  # Fallback to default
    # pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page', 1)
    try:
        products = paginator.page(page_number)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        products = paginator.page(1)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
    }
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


def main_page(request):
    return render(request,'shop/main_page.html')
