# Program Description: Honest Peter's Garage Invoice
# Written By:          Mitchell Barkley
# Written On:          May 9 2023

# Variables
InvoiceNum = 4321
Date = "10-05-2023"
CustomerName = "Ashley MacIsaac"
CustomerStreet = "92784 Imaginary Lane"
CustomerCity = "Corner Brook"
CustomerProv = "NL"
CustomerPostal = "A9A 0A0"
PlateNum = "NSRBDA"
Mileage = 834026

# Program Calculations
CostLabour = float(4839.20)
CostParts = float(3829.20)
DiscTotal = float(300.00)
HST = float(CostParts * 0.15)
InvoiceTotal = CostLabour + CostParts + HST - DiscTotal

# Program Out
print(" "*22, "HONEST PETER'S GARAGE")
print(" "*24, "123 Fixit Street")
print(" "*21, "St. John's, NL  A1A 1A1")
print(f"  Invoice#: {InvoiceNum:<4d}", " "*33, f"Date: {Date:>8s}")
print(" ","-"*65)
print(f"  Customer: {CustomerName:<30s}     Plate Number: {PlateNum:>6s}")
print(f"  Address:  {CustomerStreet:<30s}     Mileage:      {Mileage:>6d}")
print(f" "*11, f"{CustomerCity:<18s}, {CustomerProv:<2s}, {CustomerPostal:<6s}")
print()
CostLabourDsp = "${:,.2f}".format(CostLabour)
print(f" "*40, f"Cost of Labour:  {CostLabourDsp:>9s}")
CostPartsDsp = "${:,.2f}".format(CostParts)
print(f" "*40, f"Cost of Parts:   {CostPartsDsp:>9s}")
DiscTotalDsp = "${:,.2f}".format(DiscTotal)
print(f" "*39, f"Total Discount:   {DiscTotalDsp:>9s}")
HSTDsp = "${:,.2f}".format(HST)
print(f" "*51, f"HST:  {HSTDsp:>9s}")
print(f" "*56, f"-"*10)
InvoiceTotalDsp = "${:,.2f}".format(InvoiceTotal)
print(f" "*41, f"Invoice Total:  {InvoiceTotalDsp:>9s}")
print(f"-"*69)
print(f"    Honest Peter's - There to meet the needs of our Customer!!")