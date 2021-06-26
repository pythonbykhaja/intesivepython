items = ["Clothes", "phones", "laptops", "Chocolates"]

if __name__ == "__main__":
    while True:
        try:
            for index in range(0,len(items)):
                print(f"{index}  ")
            option = int(input("Enter the number of your choice to get gift: "))
            print(f"You have choosen {items[option]}")
        
        except ValueError as ve:
            print("Enter the choice of getting gift in numbers")
            print(ve)
            
        except IndexError as ie:
            print(f"Enter valid number choice ranging from 0 to {len(items)-1}")

        except Exception as e:
            print(f"Unknown Error occured {e}")

        
        else:
            print("Thank god no errors")

        finally:
            choice = input('Do you want to Continue Enter y for yes and n for no: ')
            if choice == 'n':
                break




        
