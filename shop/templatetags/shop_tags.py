from django import template
from ..models import Product

register = template.Library()


@register.inclusion_tag("partials/latest_products.html")
def latest_products(count=5):
    lasts_products = Product.objects.order_by('-created')[:count]
    context = {
        'lasts_products': lasts_products
    }
    return context


@register.inclusion_tag("partials/cheapest_products.html")
def cheapest_products(count=5):
    cheap_products = Product.objects.order_by('new_price')[:count]
    context = {
        'cheap_products': cheap_products
    }
    return context


@register.inclusion_tag("partials/most_expensive_products.html")
def most_expensive_products(count=5):
    expensive_products = Product.objects.order_by('-new_price')[:count]
    context = {
        'expensive_products': expensive_products
    }
    return context
