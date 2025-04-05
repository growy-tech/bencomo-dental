import stripe 
import os

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

def get_stripe_products():
    products= {}

    stripe_products = stripe.Product.list(active=True)

    for product in stripe_products.data:
        product_id = product.id

        prices = stripe.Price.list(product=product_id, active=True)
        
        prices_per_currency = {}
        for price in prices.data:
            currency = price.currency.upper()
            mount = price.unit_amount
            price_id = price.id

        prices_per_currency[currency] = {
            'price_id': price_id,
            'mount': mount
        }

        if prices_per_currency:
            products[product_id] = {
                'id': product_id,
                'name': product.name,
                'description': product.description or '',
                'image': product.images[0],
                'prices': prices_per_currency,
                'metadata': product.metadata

            }

    return products

def get_product_per_id(product_id):
    products = get_stripe_products()
    return products.get(product_id)