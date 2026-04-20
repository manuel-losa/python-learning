def increase_prices(prices, multiplayer):
    new_prices = []

    for price in prices:
        new_prices.append(price * multiplayer)

    return new_prices

prices = [10, 20, 30]

result = increase_prices(prices, 0.8)

print(result)