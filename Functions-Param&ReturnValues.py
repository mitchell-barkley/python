# Program Description: Functions Exercise - Parameters and Return Values
# Written By: Mitchell Barkley
# Written On: June 12th 2023

# Libraries
import datetime

# Program Constants
BONUS_RATE = 0.01
BASE_SALARY = 350.00
SALES_QUOTA = 5000.00
COMM_RATE = 0.04

# Functions
def FindIdealAge(Age):
    IdealSpouseAge = (Age / 2) + 7

    return IdealSpouseAge

def FindLetterGrade(NumberGrade):

    if NumberGrade >= 80:
        LetterGrade = "A"
    elif 70 <= NumberGrade <= 79:
        LetterGrade = "B"
    elif 60 <= NumberGrade <= 69:
        LetterGrade = "C"
    elif 50 <= NumberGrade <= 59:
        LetterGrade = "D"
    else:
        LetterGrade = "F"

    return LetterGrade

def FindGrossPay(Hours, PayRate):
    if Hours <= 40:
        GrossPay = Hours * PayRate
    else:
        RegularPay = 40 * PayRate
        OTRate = PayRate * 1.5
        OTHours = Hours - 40
        OTPay = OTHours * OTRate
        GrossPay = RegularPay + OTPay

    return GrossPay

def FindEmpBonus(TotalSales):

    Bonus = TotalSales * BONUS_RATE
    if TotalSales < 5000.00:
        Bonus = 0
    elif TotalSales > 100000.00:
        Bonus += 500.00

    return Bonus

def PrintSomeStuff():
    print("This is a heading.")
    print(20+10)
    Money = 100
    print(f"You have ${Money}")

def FindPayDate(PuchaseDate):

    PurchaseDateYear = PuchaseDate.year
    PurchaseDateMonth = PuchaseDate.month
    PurchaseDateDay = PurchaseDate.day

    PayDateDay = 1
    PayDateMonth = PurchaseDateMonth + 1
    PayDateYear = PurchaseDateYear

    if PurchaseDateDay >= 25:
        PayDateMonth += 1

    return PayDate


def FindGPSalary(Sales):

    if Sales < SALES_QUOTA:
        Under = (SALES_QUOTA - Sales) * 0.10
        Salary = BASE_SALARY - Under
        Comm = 0
    else:
        Salary = Sales * COMM_RATE

    GrossPay = BASE_SALARY + Comm

    if Sales > 20000.00:
        GrossPay += 500.00
    elif Sales > 10000.00:
        GrossPay += 200.00


    return GrossPay

def FindCustomerStat(BalanceDue, CreditLimit, LastPurchaseDate, LastPaymentDate):
    if BalanceDue > CreditLimit:
        Status = "OVER"
    elif BalanceDue + 200.00 >= CreditLimit:
        Status = "CHECK"
    else:
        Status = "OKAY"

    CurrentDate = datetime.datetime.now()
    LastPurchDate = (CurrentDate - LastPurchaseDate).days

    if LastPurchDate > 60:
        Status += "-PURCH"

    LastPaymentDate = (CurrentDate - LastPaymentDate).days

    if LastPaymentDate > 30:
        Status += "-PAY"

    return Status


# Main Program
while True:

    Age = int(input("Enter your age: "))
    IdealSpouseAge = FindIdealAge()
    print(IdealSpouseAge)

    StudGrade = float(input("Enter the student's grade (0 - 100): "))
    LGrade = FindLetterGrade(StudGrade)
    print(LGrade)

    EmployeeName = input("Enter the employee's name: ")
    HoursWorked = float(input("Enter the number of hours worked: "))
    HourlyPayRate = float(input("Enter the hourly pay rate: "))
    GrossPay = FindGrossPay(HoursWorked, HourlyPayRate)
    print(GrossPay)

    EmployeeName = input("Enter the employee's name: ")
    EmployeeSales = input("Enter the employee's total sales: ")
    Bonus = FindEmpBonus(EmployeeSales)
    print(Bonus)

    PrintSomeStuff()
    
    PurchaseDate = input("Enter the Invoice Date (YYYY-MM-DD): ")
    PurchaseDate = datetime.datetime.strptime(PurchaseDate, "%Y-%m-%d")
    
    PayDate = FindPayDate(PurchaseDate)
    print(PayDate)
    

    EmployeeSales = float(input("Enter the employee sales: "))
    GrossPay = FindGPSalary(EmployeeSales)
    print(GrossPay)



    BalanceDue = 1950.00
    CreditLimit = 2000.00
    LastPurchaseDate = "2023-02-23"
    LastPaymentDate = "2023-03-28"

    LastPurchaseDate = datetime.datetime.strptime(LastPurchaseDate, "%Y-%m-%d")
    LastPaymentDate = datetime.datetime.strptime(LastPaymentDate, "%Y-%m-%d")

    CustomerStatus = FindCustomerStat(BalanceDue, CreditLimit, LastPurchaseDate, LastPaymentDate)
    print(CustomerStatus)

    Continue = input("Do you want to continue? (Y/N): ").upper()
    if Continue == "N":
        break