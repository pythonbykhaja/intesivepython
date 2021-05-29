products = []
counts = []
prices = []
item_prices = []
while True:
    item = input('Enter the item to be purchased: ')
    count = int(input('Enter the number of items to be purchased: '))
    price = float(input('Enter the price per unit: '))
    item_price = count * price
    products.append(item)
    counts.append(count)
    prices.append(price)
    item_prices.append(item_price)
    
    choice = input('Do you want to continue press y to continue and n to exit ')
    if choice == 'n':
        break

print("Quality Fresh SuperMarket")
print()
print()
print("item \t count \t unitprice \t total price")
bill_amount = 0
for item, count, price, total_price in zip(products,counts,prices, item_prices):
    print(f"{item} \t {count} \t {price} \t \t {total_price}")
    bill_amount += total_price

print()
print()
print(f"Bill amount: {bill_amount}")