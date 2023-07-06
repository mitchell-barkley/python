# Program Description: Snuggly Company Order Form
# Written By: Mitchell Barkley
# Written On: May 18th 2023

# Constants
ONE_COST = 29.99
TWO_TEN_COST = 24.99
TEN_PLUS_COST = 21.99

SHIP_UNDER_SIX = 5.99
SHIP_OVER_SIX = 3.99

HST_RATE = 0.15
SERVICE_RATE = 0.05

# Inputs
while True:
    print()
    print("      SNUGGLY COMPANY ORDER FORM ")
    print()
    print("-"*50)
    print()
    while True:
        CustName = input("Enter the Customer's Name: ")
        if CustName == "":
            print("Error - Customer Name can not be blank.")
        else:
            break

    if CustName == "END":
        break

    CustStreet = input("Enter the Customer's Street Address: ")
    CustCity = input("Enter the Customer's City: ")

    while True:
        CustProv = input("Enter the Customer's Province: ").upper()
        try:
            CustProvTry = f"{CustProv:2>s}"
        except:
            print("Province must be in 2 letter format")
        else:
            break

    CustPostal = input("Enter the Customer's Postal Code: ").upper()
    CustPhone = input("Enter the Customer's Phone Number: ")
    CustCard = input("Enter the Customer's Credit Card Number: ")

    while True:
        NumItems = int(input("Enter the Number of Snugglys purchased (1-20): "))
        if NumItems < 1 or NumItems > 20:
            print("Error - Number of items is not valid.")
        elif NumItems == "":
            print("Error - Number of items can not be blank.")
        else:
            break

    print()
    print("-"*50)
    print()

# Program Calculations
    if NumItems == 1:
        OrderCost = ONE_COST
    elif NumItems <= 10:
        OrderCost = NumItems * TWO_TEN_COST
    else:
        OrderCost = NumItems * TEN_PLUS_COST

    if NumItems >= 6:
        ShippingCost = SHIP_OVER_SIX
    else:
        ShippingCost = SHIP_UNDER_SIX

    SubTotal = ShippingCost + OrderCost
    HSTCost = SubTotal + HST_RATE
    TotalOrderCost = SubTotal + HSTCost

    ServiceCharge = TotalOrderCost * SERVICE_RATE

    # Program Outputs
    print("Order Details Confirmation")
    print("-"*50)
    print(f"Customer Name:                 {CustName:<25s}")
    print(f"Province:                      {CustProv:<2s}")
    print()
    print(f"Number of Snugglys Ordered:    {NumItems:>9d}")
    print()
    TotalOrderCostDsp = f"${TotalOrderCost:,.2f}"
    print(f"Total Cost:                    {TotalOrderCostDsp:>9s}")
    ServiceChargeDsp = f"${ServiceCharge:,.2f}"
    print(f"Credit Card Service Charge:    {ServiceChargeDsp:>9s}")
    print("-"*50)
    print()