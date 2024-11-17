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
