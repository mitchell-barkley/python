# Program Description: Holiday Plus - Customer Confirmation
# Written By:          Mitchell Barkley
# Written On:          May 10th 2023

# Input
Location = input("Enter your Trip Destination: ")
DepDate = input("Enter your Trip Departure Date: ")
NumWeeks = input("Enter the Number of Weeks of your Trip: ")
CustName = input("Enter your Name: ")
AddressStreet = input("Enter your Street Address: ")
AddressCity = input("Enter your City: ")
AddressProv = input("Enter your Province: ")
AddressPostal = input("Enter your Postal Code: ")

# Calculations
HolidayCost = float(input("Enter the Cost of your Trip: "))
Tax = HolidayCost * 0.15
DownPay = HolidayCost * 0.1
TotalDue = HolidayCost + Tax + DownPay

# Output
print()
print("  HOLIDAY PLUS - CUSTOMER CONFIRMATION")
print()
print(f"  Location: {Location:<20s}      Departure Date: {DepDate:<8s}   # Weeks: {NumWeeks:<1s}")
print()
print("  Customer:", " "*36, "Charges:")
print()
HolidayCostDsp = f"${HolidayCost:,.2f}"
print(f"  {CustName:<25s}", " "*20, f"Holiday Cost:   {HolidayCostDsp:>10s}")
TaxDsp = f"${Tax:,.2f}"
print(f"  {AddressStreet:<25s}", " "*20, f"Tax:            {TaxDsp:>10s}")
DownPayDsp = f"${DownPay:,.2f}"
print(f"  {AddressCity:<15s},{AddressProv:<2s} {AddressPostal:<6s}"," "*20, f"Down Payment:   {DownPayDsp:>10s}")
print(" "*48, "-"*26)
TotalDueDsp = f"${TotalDue:,.2f}"
print(" "*48, f"Total Due:      {TotalDueDsp:>10s}")
print()
print("  Authorization: ", "_"*30)
print()
print("    Thank you for booking with Holiday Plus Travel. Enjoy you trip!")
