import pprint


colors = ['Red', 'Green', 'Yellow', 'Blue', 'White', 'Black']
inventory = { 'IPhone12': 20, 'OnePlus': 40, 'Samsung Note': 60 }
print(colors)
print(inventory)

pp = pprint.PrettyPrinter(indent=4, width=20, compact=True)

pp.pprint(colors)
pp.pprint(inventory)