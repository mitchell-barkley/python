# Program Description: ABC Company Payroll
# Written By: Mitchell Barkley
# Written On: May 11th 2023

# Define Program Constants
HOUR_PAY_RATE = 17.50
SALES_COMM_RATE = 0.06
ASS_COMM_RATE = 0.45
IT_RATE = 0.17
CPP_RATE = 0.0495
EI_RATE = 0.016
UNION_DUES = 12.00
MED_RATE = 0.05

# User Inputs
EmpName = input("Enter the Employee Name: ")
HoursWorked = float(input("Enter the Number of Hours Worked: "))
TotalSales = float(input("Enter the Total Sales: "))
NumItemsAss = int(input("Enter the Number of Items Assembled: "))

# Calculations
RegPay = HoursWorked * HOUR_PAY_RATE
SalesComm = TotalSales * SALES_COMM_RATE
AssComm = NumItemsAss * ASS_COMM_RATE
TotalComm = SalesComm + AssComm
GrossPay = RegPay + TotalComm

IT = GrossPay * IT_RATE
CPP = GrossPay * CPP_RATE
EI = GrossPay * EI_RATE
MedBen = GrossPay * MED_RATE
TotalDeduc = IT + CPP + EI + MedBen

NetPay = GrossPay - TotalDeduc

# Output
print()
print()
print("   ABC COMPANY")
print("   Employee Weekly Payroll Summary")
print()
print(f"   Employee Name: {EmpName:<20s}")
print()
PayRateDsp = f"${HOUR_PAY_RATE:.2f}"
HoursWorkedDsp = "{:.0f}".format(HoursWorked)
print(f"   Hours Worked: {HoursWorkedDsp:<2s}     Pay Rate: {PayRateDsp:6>s}")
print()
SalesCommRateDsp = "{:.0%}".format(SALES_COMM_RATE)
#  {%} multiplies by 100 for display

AssCommRateDsp = "{:.2f}".format(ASS_COMM_RATE)
print(f"   Commission Rates:    On Sales:    {SalesCommRateDsp:>3s}   On Assemblies:    {AssCommRateDsp:>3s}")
print()
GrossPayDsp = "${:,.2f}".format(GrossPay)
print(f"        Regular Pay:                     {GrossPayDsp:>9s}")
print()
SalesCommDsp = "${:.2f}".format(SalesComm)
print(f"           Sales Commission:     {SalesCommDsp}")
AssCommDsp = "${:.2f}".format(AssComm)
print(f"        Assembly Commission:     {AssCommDsp}")
print(" "*29, "-"*9, "-"*9)
TotalCommDsp = "${:,.2f}".format(TotalComm)
print(f"     Total Commission:                  {TotalCommDsp:>9s}")
print(" "*39, "-"*9)
GrossPayDsp = "${:,.2f}".format(GrossPay)
print(f"     Gross Pay:                         {GrossPayDsp:>9s}")
print()
print("   Deductions: ")
print()
ITDsp = "${:,.2f}".format(IT)
print(f"       Income Tax:              {ITDsp:>9s}")
CPPDsp = "${:,.2f}".format(CPP)
print(f"       CPP:                     {CPPDsp:>9s}")
EIDsp = "${:,.2f}".format(EI)
print(f"       EI:                      {EIDsp:>9s}")
UnionDuesDsp = "${:,.2f}".format(UNION_DUES)
print(f"       Union Dues:              {UnionDuesDsp:>9s}")
MedBenDsp = "${:,.2f}".format(MedBen)
print(f"       Medical Benefits:        {MedBenDsp:>9s}")
print(" "*31, "-"*9, "-"*9)
TotalDeducDsp = "${:,.2f}".format(TotalDeduc)
print(f"   Total Deductions:                      {TotalDeducDsp:>9s}")
print(" "*41, "-"*9)
NetPayDsp = "${:,.2f}".format(NetPay)
print(f"f   Weekly Net Pay:                       {NetPayDsp:>9s}")
print(" "*41, "="*9)
