items = []
while True:
    item = input('Enter the item to be purchased: ')
    count = int(input('Enter the number of items to be purchased: '))
    price = float(input('Enter the price per unit: '))
    item_price = count * price
    current_item_list = [item, count, price, item_price ]
    items.append(current_item_list)
    choice = input('Do you want to continue press y to continue and n to exit ')
    if choice == 'n':
        break

print("Quality Fresh SuperMarket")
print()
print()
print("item \t count \t unitprice \t total price")
bill_amount = 0
for current_item in items:
    item = current_item[0]
    count = current_item[1]
    price = current_item[2]
    total_price = current_item[3]
    print(f"{item} \t {count} \t {price} \t \t {total_price}")
    bill_amount += total_price

print()
print()
print(f"Bill amount: {bill_amount}")