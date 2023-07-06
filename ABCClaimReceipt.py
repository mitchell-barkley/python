# Program Description: ABC Company Claim Reciept
# Written By:          Mitchell Barkley
# Written On:          May 9th 2023

# Input
DateProcessed = "09-03-20"
SalesPerson = "Billy Joe McAllister"
Location = "Montreal"
StartDate = "08-22-20"
EndDate = "08-22-20"
NumDays = 7

# Calculations
DayCharge = 658.56
Mileage = 546
MilCharge = 132.54
HST = 102.84
ClaimTotal = 893.94

# Output
print(" "*14, "ABC Company")
print(" "*6, "Claim Confirmation Reciept")
print()
print(f"   Date Processed: {DateProcessed:<8s}")
print(f"   Sales Person:   {SalesPerson:<20s}")
print(f"   Location:       {Location:<20s}")
print(f"   Dates:          {StartDate:<8s} to {EndDate:<8s}")
print(" "*2, "-"*36)

DayChargeDsp = "${:,.2f})".format(DayCharge)
print(f"   Days:         {NumDays:>3d}   Charge:{DayChargeDsp:>9s}")

MilChargeDsp = "${:,.2f})".format(MilCharge)
print(f"   Mileage: {Mileage:>4d}              {MilChargeDsp:>9s}")

HSTDsp = "${:,.2f})".format(HST)
print(f"   Tax: (HST) @ 15%           {HSTDsp:>9s}")

print(" "*29, "-"*9)

ClaimTotalDsp = "${:,.2f})".format(ClaimTotal)
print(f"   Claim Total:                {ClaimTotalDsp:<9s}")
