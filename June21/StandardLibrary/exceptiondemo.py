items = ["Clothes", "phones", "laptops", "Chocolates"]

if __name__ == "__main__":
    while True:
        for index in range(0,len(items)):
            print(f"{index}  ")
        try:
            option = int(input("Enter the number of your choice to get gift: "))
            print(f"You have choosen {items[option]}")
            choice = input('Do you want to Continue Enter y for yes and n for no: ')
            if choice == 'n':
                break
        except IndexError:
            print("Wrong option selected try again")



        
