print("Quality Thoughts")
items = []
counts = []
price_list = []
total_bill = 0
while True:
    item=int(input("enter the purched item"))
    count=int(input("enter the no of purched item"))
    price=float(input("enter the purched item price per unit"))
    items.append(item)
    counts.append(count)
    price_list.append(price)
    
    item_bill = count * price
    total_bill += item_bill
    choice =int(input("Do you want to purched item press y to continue and n to exit:"))
    if choice == 'n':
        break
 
print(total_bill)