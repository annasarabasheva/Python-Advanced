def shopping_list(number, **kwargs):
    budget = number
    products = {}
    if number >= 100:
        for key, value in kwargs.items():
            price = value[0]
            quantity = value[1]
            total_price = price * quantity
            if budget >= total_price:
                products[key] = total_price
                budget -= total_price
            if len(products) == 5:
                break
    else:
        return "You do not have enough budget."
    result = ''
    for key, value in products.items():
        result += f"You bought {key} for {value:.2f} leva.\n"

    return result



print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
