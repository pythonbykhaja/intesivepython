from random import choice, choices, randint


def pick_one(items):
    return choice(items)

def pick_multiple(items, count=1):
    return choices(items,k=count)



if __name__ == "__main__":
    vacation_destinations = ['Vizag', 'Munnar', 'Ladakh', 'Goa', 'Pondicherry']
    print(pick_one(vacation_destinations))

    print(pick_multiple(vacation_destinations,2))

    print(f"your lucky number is {randint(1,10)}")
