def apply_discounts(prices, vip_user=False):
    updated_prices = []
    for price in prices:
        if price > 50:
            if vip_user:
                price -= price * 0.20
            else:
                price -= price * 0.10
            updated_prices.append(price)
            return updated_prices

def calculate_cart_total(cart):
    total = 0
    prices = [item["price"] for item in cart]
    breakpoint()

    discounted_prices = apply_discounts(prices, vip_user=True)

    for price in discounted_prices:
        price += price * 0.08
        total += price

    return total
shopping_cart = [
    {"name":"Laptop","price":1000},
    {"name":"mouse","price":20},
    {"name":"Keyboard","price":50}

]

result = calculate_cart_total(shopping_cart)
print(f"Resultado obtenido: {result}(esperado: 939.6)")