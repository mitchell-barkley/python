# Program Description: Widget Incorporated Payroll
# Written By:          Mitchell Barkley
# Written On:          May 8th 2023

print("Widget Incorporated Payroll")
print()

# Constants
PAY_RATE = float(19.50)
COMM_RATE = float(0.35)
INCTAX_RATE = float(0.21)
CPP_RATE = float(0.0495)
EICONT_RATE = float(0.016)
UNION_DUE = float(18.00)

# Program Input
EmpName = input("Enter The Employee's Name: ")
NumHours = float(input("Enter The Number Of Hours Worked: "))
print()
WidgetMon = int(input("Enter The Number Of Widgets Made On Monday: "))
WidgetTues = int(input("Enter The Number Of Widgets Made On Tuesday: "))
WidgetWed = int(input("Enter The Number Of Widgets Made On Wednesday: "))
WidgetThurs = int(input("Enter The Number Of Widgets Made On Thursday: "))
WidgetFri = int(input("Enter The Number Of Widgets Made On Friday: "))
print()

# Program Calculations
WidgetTotal = WidgetMon + WidgetTues + WidgetWed + WidgetThurs + WidgetFri
WagePay = round(float(NumHours * PAY_RATE),2)
CommTotal = WidgetTotal * COMM_RATE
GrossPay = WagePay + CommTotal
IncomeTax = GrossPay * INCTAX_RATE
CPP = GrossPay * CPP_RATE
EI = GrossPay * EICONT_RATE
DeducTotal = IncomeTax + CPP + EI + UNION_DUE
NetPay = GrossPay - DeducTotal

#program Output
print("Employee Name:                ",EmpName)
print("Number Of Hours Worked:       ",NumHours,"Hours")
print("Total Widgets Made:           ",WidgetTotal,"Widgets")
print()
print("Weekly Wage For Labour:       ","$",WagePay)
print("Weekly Commission Earned:     ","$",CommTotal)
print("Gross Pay:                    ","$",GrossPay)
print()
print("Deductions:")
print("Income Tax:                   ","$",IncomeTax)
print("CPP:                          ","$",CPP)
print("EI:                           ","$",EI)
print("Union Dues:                   ","$",UNION_DUE)
print("Total Deductions:             ","$",DeducTotal)
print()
print("Net Pay:                      ","$",NetPay)
print()