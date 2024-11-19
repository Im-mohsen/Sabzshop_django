from django import template
from ..models import Product
from urllib.parse import urlencode, parse_qs

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


@register.filter
def safe_remove(query_string, param):
    """
    Removes a specific parameter from the query string.
    """
    params = parse_qs(query_string)  # تبدیل query_string به دیکشنری
    params.pop(param, None)  # حذف پارامتر مورد نظر
    return urlencode(params, doseq=True)  # بازسازی query_string بدون پارامتر