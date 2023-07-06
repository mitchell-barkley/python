# Program Desription: Edsel Car Rental Company Invoice Calculator
# Written By:         Mitchell Barkley
# Written On:         May 8th 2023

# Constants
HST_RATE = 0.15
DAILY_RATE = 35.00
KM_RATE = 0.10
FREE_KM_PER_DAY = 100

print("EDSEL CAR RENTAL COMPANY INVOICE CALCULATOR")
print()

# Program Input
CustName = input("Enter The Customer's Name: ")
CustPhone = input("Enter The Customer's Phone Number: ")
DaysRental = float(input("Enter The Number Of Days The Car Was Rented: "))
StartMile = float(input("Enter The Odometer Reading At Start Of Rental: "))
EndMile = float(input("Enter The Odometer Reading At End Of Rental: "))
print()

# Program Calculations
if EndMile > StartMile:
    TotalMile = EndMile - StartMile
else:
    TotalMile = (100000 - StartMile) + EndMile

FreeKm = DaysRental * FREE_KM_PER_DAY
if TotalMile > FreeKm:
    MileCost = (TotalMile - FreeKm) * KM_RATE
else:
    MileCost = 0

DailyCost = DaysRental * DAILY_RATE
SubTotal = DailyCost + MileCost
HST = (DaysRental * DAILY_RATE) * HST_RATE
TotalDue = SubTotal + HST

# Program Output
print(f"Customer Name:                      {CustName:<20s}")
print(f"Customer Phone Number:              {CustPhone:<10s}")
DaysRentalDsp = f"{DaysRental:.0f}"
print(f"Number of Days of Rental:           {DaysRentalDsp:<2s}")
print()
StartMileDsp = f"{StartMile:.0f}km"
print(f"Odometer Start:                     {StartMileDsp:<6s}")
EndMileDsp = f"{EndMile:.0f}km"
print(f"Odometer End:                       {EndMileDsp:<6s}")
TotalMileDsp = f"{TotalMile:.0f}km"
print(f"Kilometers Driven:                  {TotalMileDsp:<6s}")
print()
MileCostDsp = f"{MileCost:.2f}"
print(f"Distance Charge:                    {MileCostDsp:<6s}")
SubTotalDsp = f"${SubTotal:.2f}"
print(f"Subtotal:                           {SubTotalDsp:<9s}")
HSTDsp = f"${HST:.2f}"
print(f"HST:                                {HSTDsp:<9s}")
TotalDueDsp = f"${TotalDue:.2f}"
print(f"Total Amount Due:                   {TotalDueDsp:<9s}")
print()