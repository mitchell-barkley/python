# Program Description: NL Power Company Meter Charges (L11Q2)
# Written By: Mitchell Barkley
# Written On: May 18th 2023

# Constants
KW_UNDER_RATE = 0.073
KW_OVER_RATE = 0.069

DISC_OVER_RATE = 0.03
DISC_UNDER_RATE = 0.01

HST_RATE = 0.15

# Program Inputs
print()
print("      NL POWER COMPANY USAGE CALCULATOR")
print()
print("-"*60)
print()
CustName = input("Enter The Customer's Name: ")
CustStreet = input("Enter The Customer's Street Address: ")
print()
LastRead = float(input("Enter the previous meter reading: "))
CurrRead = float(input("Enter the current meter reading: "))
print()
print("-"* 60)
print()

# Program Calculations
DiffRead = CurrRead - LastRead

if DiffRead > 100:
    UnderCharge = KW_UNDER_RATE * 100
    OverCharge = KW_OVER_RATE * (DiffRead - 100)
    KWCharge = UnderCharge + OverCharge
else:
    KWCharge = KW_UNDER_RATE * DiffRead

if KWCharge > 500:
    Discount = KWCharge * DISC_OVER_RATE
else:
    Discount = KWCharge * DISC_UNDER_RATE

SubTotal = KWCharge
HSTCharge = SubTotal * HST_RATE
DiscTotal = KWCharge - Discount + HSTCharge
DueTotal = KWCharge + HSTCharge

# Program Output
print(f"Customer Name:   {CustName:<20s}")
print(f"Street Address:  {CustStreet:<20s}")
print()
LastReadDsp = f"{LastRead:.0f}KWH"
print(f"                 Previous Meter Reading:           {LastReadDsp:>8s}")
CurrReadDsp = f"{CurrRead:.0f}KWH"
print(f"                 Current Meter Reading:            {CurrReadDsp:>8s}")
print(f" "*49, "-"*10)
DiffReadDsp = f"{DiffRead:.0f}KWH"
print(f"                 Usage This Month:                 {DiffReadDsp:>8s}")
print()
KWChargeDsp = f"${KWCharge:,.2f}"
print(f"Subtotal for this month's usage:     {KWChargeDsp:>9s}")
HSTDsp = f"${HSTCharge:,.2f}"
print(f"HST (15%):                           {HSTDsp:>9s}")
DueTotalDsp = f"${DueTotal:,.2f}"
print(f"Total Due this month:                {DueTotalDsp:>9s}")
print()
print()
DiscountDsp = f"${Discount:,.2f}"
DiscTotalDsp = f"${DiscTotal:,.2f}"
print(f"Discount if paid by the 24th:        {DiscountDsp:>9s}")
print(f"Amount due if paid by the 24th:      {DiscTotalDsp:>9s}")
print()
print("-"*60)