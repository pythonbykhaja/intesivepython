items = ["Clothes", "phones", "laptops", "Chocolates"]

if __name__ == "__main__":
    while True:
        try:
            for index in range(0,len(items)):
                print(f"{index}  ")
            option = int(input("Enter the number of your choice to get gift: "))
            print(f"You have choosen {items[option]}")
        
        except:
            print("Wrong option entered try again")

        else:
            print("Thank god no errors")
            
        finally:
            choice = input('Do you want to Continue Enter y for yes and n for no: ')
            if choice == 'n':
                break




        
