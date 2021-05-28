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

print(items,items_count, price)