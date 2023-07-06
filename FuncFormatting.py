# Program Description: Using Functions to Format Output
# Written By: Mitchell Barkley
# Written On: June 14th 2023

# Libraries
import FormatValues as FV
import datetime
import math
import random

# Constants

# Functions
def FDollar2(DollarValue):

    DollarValueString = "${:,.2f}".format(DollarValue)

    return DollarValueString

# Main Program
while True:
    ItemCost = 359.00
    Salary = 57500.00
    Today = datetime.datetime.now()
    Number = 4756

    print(f"Item Cost: {FDollar2(ItemCost):>10s}")
    print(f"Salary:    {FDollar2(Salary):>10s}")
    print(f"Current Date: {FV.FDateL(Today):<9s}")
    print(f"Current Date: {FV.FDateL(Today):<9s}")
    print(f"Current Date: {FV.FDateM(Today):<9s}")
    print(f"Current Date: {FV.FDateS(Today):<9s}")
    print(f"Number:       {FV.FComma2(Number):>10s}")
    print(f"Number:       {FV.FComma0(Number):>10s}")
    print(f"Number:       {FV.FNumber1(Number):>10s}")

    RandomNumber = random.randint(1, 1000)
    print(RandomNumber)

    Continue = input("Do you want to continue? (Y/N): ").upper()
    if Continue == "N":
        break