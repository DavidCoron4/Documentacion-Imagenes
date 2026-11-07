def calcule_total(prices, discount):
    total = 0
    for price in prices:
        breakpoint()
        discounted = price -(price * discount)
        total += discounted
    return total
items = [100,200,300]
result = calcule_total(items, 0.1)
print(f"Total: {result}")
