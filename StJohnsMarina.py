# Program Description: St. John's Marina & Yacht Club Yearly Member Receipt
# Written By: Mitchell Barkley
# Written On: May 24th 2023

# Constants
HST_RATE = 0.15

EVEN_SITE_RATE = 80.00
ODD_SITE_RATE = 120.00
EXTRA_MEM_RATE = 5.00

SITE_CLEAN_YES = 50.00
VIDEO_SURVEIL_YES = 35.00

PROCESS_FEE = 59.99

# Program Inputs
print()
print("  St. John's Marina & Yacht Club")
print("       Member Information")
print("-"*36)
print()
print("Please enter all required information below:")
print()
ClientName = input("Client Name: ")
ClientStreet = input("Street Address: ")
ClientCity = input("City: ")
ClientProv = input("Province: ")
ClientPostal = input("Postal Code: ")
ClientHomePhone = input("Home Phone Number: ")
ClientCellPhone = input("Cell Phone Number: ")
print()
SiteNum = int(input("Site Number (1-100): "))
MemberType = input("Member Type ('S' - Standard or 'E' - Executive): ").upper()
NumMembers = int(input("Number of Alternate Members: "))
print()
print("-"*36)
print()
print("Optional Extras:")
print()
SiteClean = input("Weekly Site Cleaning ('Y' or 'N'): ").upper()
VideoSurveil = input("24/7 Video Surveillance ('Y' or 'N'): ").upper()
print()
print()
print("-"*36)

# Program Calculations
SiteNumDsp = f"{SiteNum:d}"
NumMembersDsp = f"{NumMembers:d}"

if MemberType == "S":
    MemberTypeDsp = "Standard"
    MonthlyDue = 75.00
elif MemberType == "E":
    MemberTypeDsp = "Executive"
    MonthlyDue = 150.00
else:
    MemberTypeDsp = "None"
    MonthlyDue = 0.00

ExtraCharges = 0.00
if SiteClean == "Y":
    ExtraCharges += SITE_CLEAN_YES
    SiteCleanDsp = "Yes"
elif SiteClean == "N":
    ExtraCharges += 0.00
    SiteCleanDsp = "No"
else:
    SiteCleanDsp = "Error"
    ExtraCharges = 0.00

if VideoSurveil == "Y":
    ExtraCharges += VIDEO_SURVEIL_YES
    VideoSurveilDsp = "Yes"
elif VideoSurveil == "N":
    ExtraCharges += 0.00
    VideoSurveilDsp = "No"
else:
    VideoSurveilDsp = "Error"
    ExtraCharges = 0.00

if SiteNum % 2 == 0:
    SiteCharge = (NumMembers * 5.00) + EVEN_SITE_RATE
else:
    SiteCharge = (NumMembers * 5.00) + ODD_SITE_RATE

SubTotal = SiteCharge + ExtraCharges
HST = SubTotal * HST_RATE
TotalMonthlyCharge = SubTotal + HST
TotalMonthlyFee = TotalMonthlyCharge + MonthlyDue
TotalYearlyFee = TotalMonthlyFee * 12
MonthlyPayment = (TotalYearlyFee + PROCESS_FEE) / 12
CancelFee = (SiteCharge * 12) * 0.6

SiteChargeDsp = f"${SiteCharge:,.2f}"
ExtraChargesDsp = f"${ExtraCharges:,.2f}"
SubTotalDsp = f"${SubTotal:,.2f}"
HSTDsp = f"${HST:,.2f}"
TotalMonthlyChargeDsp = f"${TotalMonthlyCharge:,.2f}"
MonthlyDueDsp = f"${MonthlyDue:,.2f}"
TotalMonthlyFeeDsp = f"${TotalMonthlyFee:,.2f}"
TotalYearlyFeeDsp = f"${TotalYearlyFee:,.2f}"
MonthlyPaymentDsp = f"${MonthlyPayment:,.2f}"
CancelFeeDsp = f"${CancelFee:,.2f}"

# Program Output
print()
print("  St. John's Marina & Yacht Club")
print("       Yearly Member Receipt")
print()
print("-"*36)
print()
print(" Client Name and Address:")
print()
print(f" {ClientName:<28s}")
print(f" {ClientStreet:<28s}")
print(f" {ClientCity:<20s}, {ClientProv:<2s} {ClientPostal:<6s}")
print()
print(f" Phone: {ClientHomePhone:<10s} (H)")
print(f"        {ClientCellPhone:<10s} (C)")
print()
print(f" Site #: {SiteNumDsp:<3s} Member type: {MemberTypeDsp:<9s}")
print()
print(f" Alternate members:              {NumMembersDsp:>2s}")
print(f" Weekly site cleaning:          {SiteCleanDsp:>3s}")
print(f" Video Surveillance:            {VideoSurveilDsp:>3s}")
print()
print(f" Site charges:            {SiteChargeDsp:>9s}")
print(f" Extra charges:           {ExtraChargesDsp:>9s}")
print(f" "*25, "-"*9)
print(f" Subtotal:                {SubTotalDsp:>9s}")
print(f" Sales tax (HST):         {HSTDsp:>9s}")
print(f" "*25, "-"*9)
print(f" Total monthly charges:   {TotalMonthlyChargeDsp:>9s}")
print(f" Monthly dues:            {MonthlyDueDsp:>9s}")
print(f" "*25, "-"*9)
print(f" Total monthly fees:      {TotalMonthlyFeeDsp:>9s}")
print(f" Total yearly fees:       {TotalYearlyFeeDsp:>9s}")
print()
print(f" Monthly payment:         {MonthlyPaymentDsp:>9s}")
print()
print("-"*36)
print()
from datetime import datetime
print(f" Issued: {datetime.today().strftime('%Y-%m-%d')}")
print(" HST Reg No: 549-33-5849-4720-9885")
print()
print(f" Cancellation fee:        {CancelFeeDsp:>9s}")
