# Program Description: Billy Bob Bike Rental
# Written By: Mitchell Barkley
# Written On: May 29th 2023

# User Inputs
while True:

    while True:
        CustName = input("Enter the Customer's Name: ")
        if CustName == "":
            print("Error - Customer Name can not be blank")
        else:
            break

    while True:
        PhoneNumber = input("Enter the Customer's Phone Number (999-9999): ")

        if PhoneNumber == "":
            print("Error - Phone Number can not be blank")
        else:
            break

    while True:
        BikeCode = input("Enter the type of bicycle rented (T, M, B): ").upper()

        if BikeCode == "":
            print("Error - Bicycle Type can not be blank.")
        elif BikeCode != "T" and BikeCode != "M" and BikeCode != "B":
            print("Bicycle Type must be a 'T', 'M' or 'B'.")
        else:
            break

    while True:
        try:
            NumRented = int(input("Enter the Number of Bicycles rented (1-3): "))
        except:
            print("Error - Must be a valid number.")
        else:
            if NumRented < 1 or NumRented > 3:
                print("Error - Number of bicycles must be between 1 and 3.")
            else:
                break

    CCNum = input("Enter Credit Card Number: ")
    ExpDate = input("Enter the expiry date: ")

    # Calculations
    print()
    while True:
        Continue = input("Do you want to process another bicycle rental? (Y or N): ").upper()
        if Continue == "":
            print("Error - can not be blank.")
        elif Continue != "Y" and Continue != "N":
            print("Error - must be a 'Y' or 'N'")
        else:
            break

    if Continue == "N":
        break
