from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from django.http import JsonResponse
from .common.KaveSms import send_sms_normal, send_sms_with_template


# Create your views here.
@require_POST
def add_to_cart(request, product_id):
    try:
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product)
        context = {
            'item_count': len(cart),
            'total_price': cart.get_total_price(),
        }
        # send SMS (Not need to working here)
        # send_sms_normal('09010107036', f'اضافه شدن محصول به سبد خرید شما: {product.name}')
        # send_sms_with_template(product.phone, {'token1': product.name, 'token10': '54325'}, 'send_template_sms')
        return JsonResponse(context)
    except:
        return JsonResponse({'error': 'Invalid request'})


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


@require_POST
def update_quantity(request):
    item_id = request.POST.get('item_id')
    action = request.POST.get('action')
    try:
        product = get_object_or_404(Product, id=item_id)
        cart = Cart(request)
        if action == 'add':
            cart.add(product)
        elif action == 'sub':
            cart.sub(product)
        context = {
            'success': True,
            'item_count': len(cart),
            'total_price': cart.get_total_price(),
            'quantity': cart.cart[item_id]['quantity'],
            # 'price': cart.cart[item_id]['price'],
            'total': cart.cart[item_id]['price'] * cart.cart[item_id]['quantity'],
            'final_price': cart.get_final_price(),
            'post_price': cart.get_post_price(),
        }
        return JsonResponse(context)
    except:
        return JsonResponse({'success': False, 'error': 'Item not found!'})


@require_POST
def remove_item(request):
    item_id = request.POST.get('item_id')
    try:
        product = get_object_or_404(Product, id=item_id)
        cart = Cart(request)
        cart.remove(product)

        context = {
            'success': True,
            'item_count': len(cart),
            'total_price': cart.get_total_price(),
            'final_price': cart.get_final_price(),
            'post_price': cart.get_post_price(),
        }
        return JsonResponse(context)
    except:
        return JsonResponse({'success': False, 'error': 'Item not found!'})
