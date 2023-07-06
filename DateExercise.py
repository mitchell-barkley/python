# Program Description: Date Object Exercises
# Written By: Mitchell Barkley
# Written On: June 5th 2023

import datetime


# Define the current date and print with different formats
CurDate = datetime.datetime.now()
print()
print("Current date based on the system date")
print("Note how it prints the date and time")
print(CurDate)
print()
print("Different formats when printing out a date")
print(CurDate.strftime("%A %a %Y %y %m %B %b %d"))
print(CurDate.strftime("%Y/%m/%d"))
print(CurDate.strftime("%B %d, %Y"))
print(CurDate.strftime("%A %B %d, %Y"))
CurDateDsp = CurDate.strftime("%Y-%m-%d")
print(f"The current date is {CurDateDsp}.")

# Add 4 days and 30 days to the Current date
CurDatePlus4 = CurDate + datetime.timedelta(days = 4)
print()
print("Current date plus 4 days")
print(CurDatePlus4)
CurDatePlus30 = CurDate + datetime.timedelta(days = 30)
print()
print("Current date plus 30 days")
print(CurDatePlus30)

# Define two dates as strings - same as if these were input
arrivalstr = "2021-2-3"
departurestr = "2021-3-12"

# Convert the arrival and departure from string objects to datetime objects
arrival = datetime.datetime.strptime(arrivalstr, "%Y-%m-%d")
print()
print("Arrival date converted from string object to datetime object")
print(arrivalstr)
print(arrival)
departure = datetime.datetime.strptime(departurestr, "%Y-%m-%d")
print()
print("Departure date converted from string object to datetime object")
departureDsp = departure.strftime("%B %d, %Y")
print(departurestr)
print(departure)
print(departureDsp)

# Calculate the number of days between the two dates
days = (departure - arrival).days
print()
print("Difference between arrival and departure date in days")
print(days)

# Pull out the different parts of a date
CurYear = CurDate.year
print()
print("Parts of a date including the Year, Month and Day from CurDate")
print(CurYear)
CurMonth = CurDate.month
print(CurMonth)
CurDay = CurDate.day
print(CurDay)
NewDate = datetime.date(CurYear, CurMonth + 3, CurDay)
print(NewDate)

StartDate = input("Enter the start date (YYYY-MM-DD): ")
StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
EndDate = input("Enter the date date (YYYY-MM-DD): ")
EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
Days = (EndDate - StartDate).days
TotalClaim = Days * 56.00
print(Days)
print(TotalClaim)


while True:
    try:
        InvoiceDate = input("Enter the Invoice Date (YYYY-MM-DD): ")
        InvoiceDate = datetime.datetime.strptime(InvoiceDate, "%Y-%m-%d")
    except:
        print("Error - Invalid Date Format.")
    else:
        break

while True:
    try:
        InvoiceAmount = float(input("Enter the Invoice Amount: "))
    except:
        print("Error - Invalid entry for Invoice Amount.")
    else:
        break

DiscountDate = InvoiceDate + datetime.timedelta(days=10)
Discount = InvoiceAmount * 0.02
DiscountAmount = InvoiceAmount - Discount

DueDate = InvoiceDate + datetime.timedelta(days=30)

CurrentDate = datetime.datetime.now()
InvoiceAge = (CurrentDate - InvoiceDate).days

InvoiceDsp = "${InvoiceAmount:,.2f}"
DiscountAmountDsp = "${DiscountAmount:,.2f}"
DiscountDateDsp = DiscountDate.strftime("%B %d, %Y")
DueDateDsp = DueDate.strftime("%B %d, %Y")

print(f"Invoice Amount:                 {InvoiceAmount}")
print(f"Discount Date:                  {DiscountDate}")
print(f"Discounted Invoice Amount:      {DiscountAmount}")
print(f"Invoice Due Date:               {DueDate}")
print(f"Invoice Age:                    {InvoiceAge}")



while True:

    ExpiryDate = input("Enter the ExpiryDate (MM/YY): ")

    try:
        ExpiryMonth = int(ExpiryDate[0:2])
        ExpiryYear = int(ExpiryDate[3:5])
        CurrentYear = datetime.datetime.now().year - 2000
        CurrentMonth = datetime.datetime.now().month

    except:
        print("Error - Invalid Format. (MM/YY)")
    else:
        if ExpiryDate[2] != "/":
            print("Error - Invalid Format. (MM/YY)")
        elif ExpiryMonth < 1 or ExpiryMonth > 12:
            print("Error - Invalid Month. (01 - 12)")
        elif ExpiryYear > CurrentYear + 4:
            print("Error - Invalid Year (Must be within next 4 years.)")
        elif ExpiryYear < CurrentYear:
            if ExpiryMonth < CurrentMonth:
                print("Error - Card is expired.")
            else:
                break
print(f"Expiry Date: {ExpiryMonth}/{ExpiryYear}")