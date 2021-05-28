items = []
items_count = []
price_per_item = []
while True:
    item = input('Enter the item to be purchased: ')
    count = int(input('Enter the number of items to be purchased: '))
    price = float(input('Enter the price per unit: '))
    items.append(item)
    items_count.append(count)
    price_per_item.append(price)
    choice = input('Do you want to continue press y to continue and n to exit ')
    if choice == 'n':
        break

print("Quality Fresh SuperMarket")
print()
print()
print("item \t count \t unitprice \t total price")
bill_amount = 0
for index in range(len(items)):
    item = items[index]
    count = items_count[index]
    price = price_per_item[index]
    total_price = count * price
    print(f"{item} \t {count} \t {price} \t \t {total_price}")
    bill_amount += total_price

print()
print()
print(f"Bill amount: {bill_amount}")