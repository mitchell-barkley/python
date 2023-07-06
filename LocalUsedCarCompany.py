# Program Description: Local Used Car Company
# Written By: Mitchell Barkley
# Written On: May 29th 2023

print()
print("     Local Used Car Company")
print()

# Program Inputs
while True:

    while True:
        CustNum = input("Enter the Customer Number (12345): ")
        if CustNum == "":
            print("Error - Customer Number can not be blank.")
        elif len(CustNum) != 5:
            print("Error - Customer Number must be 5 digits.")
        elif not CustNum.isdigit():
            print("Error - Customer Number must be 5 digits.")

    while True:
        allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'-")
        CustName = input("Enter the Customer's Name (Type END to Quit): ").upper()
        if CustName == "":
            print("Error - Customer Name can not be blank.")
        elif not set(CustName).issubset(allowed_char):
            print("Error - Customer Name contains invalid characters.")
        elif CustName != "END":
            break
        else:
            break

    if CustName == "END":
        break

    while True:
        CustPhone = input("Enter the Customer's Phone Number (1234567890): ")
        if CustPhone == "":
            print("Error - Customer Phone Number can not be blank.")
        elif len(CustPhone) != 10:
            print("Error - Phone Number must be 10 digits.")
        elif not CustPhone.isdigit():    # or elif CustPhone.isdigit() != False
            print("Error - Phone Number must be 10 digits.")
        else:
            break

    # Function syntax is FuncName(Parameters)
    # Method syntax is VariableName.MethodName()

    while True:
        CarYear = input("Enter the Year of the Rental Car: ")
        if CarYear == "":
            print("Error - Rental Info can not be blank.")
        else:
            break
        CarMake = input("Enter the Make of the Rental Car: ").upper()
        if CarMake == "":
            print("Error - Rental Info can not be blank.")
        else:
            break
        CarModel = input("Enter the Model of the Rental Car: ").upper()
        if CarModel == "":
            print("Error - Rental Info can not be blank.")
        else:
            break

    while True:
        allowed_char = set("1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        PlateNum = input("Enter the Licence Plate Number (JMW345): ").upper()
        if PlateNum == "":
            print("Error - Licence Plate Number can not be blank.")
        elif len(PlateNum) != 6:
            print("Error - Licence Plate must be 6 characters.")
        elif not set(PlateNum).issubset(allowed_char):
            print("Error - Licence Plate Number contains invalid characters.")

    while True:
        try:
            CarPrice = float(input("Enter the Price of the Rental Car ($1,000 - $10,000): "))
        except:
            print("Error - Rental Price is not a valid number.")
        else:
            if CarPrice < 1000.00 or CarPrice > 10000.00:
                print("Error - Rental Price is outside of the allowable range.")
            else:
                break
    while True:
        try:
            Trade = float(input("Enter the Trade-In Allowance: "))
        except:
            print("Error - Trade-In Amount is not a valid number.")
        else:
            if Trade > 10000.00:
                print("Trade-In Amount can not exceed $10,000.00.")
print()
print("Thank You for renting from Local Used Car Company!")
