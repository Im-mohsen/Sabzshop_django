from shop.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'weight': product.weight}
        else:
            if self.cart[product_id]['quantity'] < product.inventory:
                self.cart[product_id]['quantity'] += 1
        self.save()

    def sub(self, product):
        product_id = str(product.id)
        if self.cart[product_id]['quantity'] > 1:
            self.cart[product_id]['quantity'] -= 1
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def clear(self):
        del self.session['cart']
        self.save()

    def get_post_price(self):
        weight = sum(item['weight'] * item['quantity'] for item in self.cart.values())
        if weight < 1000:
            return 20000
        elif 1000 < weight < 2000:
            return 30000
        else:
            return 50000

    def get_total_price(self):
        """
        Calculate the total price dynamically based on the current prices in the database.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        total_price = 0
        for product in products:
            product_id = str(product.id)
            total_price += product.new_price * self.cart[product_id]['quantity']
        return total_price

    def get_final_price(self):
        return self.get_total_price() + self.get_post_price()

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        """
        Dynamically update product prices while iterating.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart_dict = self.cart.copy()
        for product in products:
            product_id = str(product.id)
            cart_dict[product_id]['product'] = product
            cart_dict[product_id]['price'] = product.new_price  # قیمت به‌روز
            cart_dict[product_id]['total'] = product.new_price * cart_dict[product_id]['quantity']
        for item in cart_dict.values():
            yield item

    def save(self):
        self.session.modified = True
