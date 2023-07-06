# Program Description: NL Chocolate Company - Sprint Project 1
# Written By: Group 4 - Steven Squires, Mitchell Barkley and Marlanna Ryan
# Written On: June 17th 2023

# Constants

PER_DIEM_RATE = 85.00
RENT_DAY_RATE = 65.00
PER_KM_RATE = 0.17
HST_RATE = 0.15
EXEC_DAY_BONUS = 45.00

# Libraries

import datetime
import re  # Imports the regular expression module.

# Functions

# Function to validate and adjust a string to title case
def validate_and_title_case(string):
    if string.strip():
        return string.strip().title()
    else:
        return None


# Function to validate and adjust a string to uppercase
def validate_and_uppercase(string):
    if string.strip():
        return string.strip().upper()
    else:
        return None


# Function to validate the date format
def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Function for Option 1 of Main Menu
def EmpTravelClaim():
    print()
    print("   === Travel Claim Form Inputs ===")
    print("   --------------------------------")

    while True:
        while True:
            EmployeeNum = input("Enter the employee's number (ex. 54321): ")
            if EmployeeNum.strip() == "":
                print("ERROR - Employee number cannot be blank.")
            elif len(EmployeeNum) != 5:
                print("Invalid input. Employee number must be 5 digits (ex. 54321).")
            elif not EmployeeNum.isdigit():
                print("ERROR - Employee number must consist of numerical digits only. (ex. 54321)")
            else:
                break

        while True:
            EmployeeFirst = input("Enter employee's first name: ").title()
            if EmployeeFirst.strip() == "":
                print("ERROR - Employee first name cannot be blank.")
            else:
                break

        while True:
            EmployeeLast = input("Enter employee's last name: ").title()
            if EmployeeLast.strip() == "":
                print("ERROR - Employee last name cannot be blank.")
            else:
                break

        while True:
            TripLocation = input("Enter the trip location: ").title()
            if TripLocation.strip() == "":
                print("ERROR - Trip location cannot be blank.")
            else:
                break

        while True:
            VehicleUsedDsp = ""
            VehicleUsed = input("Enter O if employee used Own vehicle or R if a rental used. (O/R): ").upper()
            if VehicleUsed.strip() == "":
                print("ERROR - Must enter O or R. This cannot be blank.")
            elif VehicleUsed != "O" and VehicleUsed != "R":
                print("ERROR - Invalid character. Must be O or R.")
                VehicleUsedDsp = ""
            else:
                if VehicleUsed == 'O':
                    VehicleUsedDsp = "Owned"
                    while True:
                        TotKmTraveled = int(input("Enter Total Kilometers Traveled (cannot exceed 2000): "))
                        if TotKmTraveled == "":
                            print("ERROR - Total Kilometers Traveled cannot be blank (cannot exceed 2000).")
                        elif not TotKmTraveled or not 0 <= int(TotKmTraveled) <= 2000:
                            print("ERROR - Invalid input. Total kilometers must be a number between 0 and 2000.")
                        else:
                            TotKmTraveled = int(TotKmTraveled)
                            break
                elif VehicleUsed == 'R':
                    VehicleUsedDsp = "Rented"
                    TotKmTraveled = "N/A"
                break

        while True:
            StartDate = input("Enter the start date of the trip (Format is YYYY-MM-DD): ")
            if StartDate == "":
                print("ERROR - Start date cannot be blank.")
            elif not validate_date(StartDate):
                print("ERROR - Invalid date format. Please use the format YYYY-MM-DD.")
            else:
                StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
                break

        while True:
            EndDate = input("Enter end date of trip (Format is YYYY-MM-DD): ")
            if EndDate == "":
                print("ERROR - End date cannot be blank.")
            elif not validate_date(EndDate):
                print("Invalid date format. Please use the format YYYY-MM-DD.")
            else:
                EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
                if EndDate < StartDate:
                    print("ERROR - Time travel doesn't work here Dr. Who. Try again.(Format is YYYY-MM-DD)")
                else:
                    break

        TravelDays = (EndDate - StartDate).days + 1

        while TravelDays < 1 or TravelDays > 7:
            print("Invalid number of days traveled. Must be between 1 and 7.")
            EndDate = input("Enter end date of trip (Format is YYYY-MM-DD): ")
            if EndDate == "":
                print("ERROR - End date cannot be blank.")
            elif not validate_date(EndDate):
                print("Invalid date format. Please use the format YYYY-MM-DD.")
            else:
                EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
                TravelDays = (EndDate - StartDate).days + 1
                break

        while True:
            ClaimTypeDsp = ""
            ClaimType = input("Enter claim type as either S for Standard or E for Executive. (S/E): ").upper()
            if ClaimType != "S" and ClaimType != "E":
                print("ERROR - Invalid input. Claim type must be S or E.")
            else:
                if ClaimType == "S":
                    ClaimTypeDsp = "Standard"
                elif ClaimType == "E":
                    ClaimTypeDsp = "Executive"
                break

        # Calculations and Processes
        PerDiemAmt = TravelDays * PER_DIEM_RATE

        MileageAmt = 0.00
        if VehicleUsed == "O" and int(TotKmTraveled) > 1000:
            MileageAmt = int(TotKmTraveled) * PER_KM_RATE
        else:
            VehicleUsed = "R"
            MileageAmt = RENT_DAY_RATE * TravelDays

        Bonus = 0.00
        if ClaimType == "E":
            Bonus += TravelDays * EXEC_DAY_BONUS

        if StartDate.month == 12 and 15 <= StartDate.day <= 22:
            Bonus += TravelDays * 50.00

        if TravelDays > 3:
            Bonus += 100.00

        if VehicleUsed == "O" and int(TotKmTraveled) > 1000:
            Bonus += int(TotKmTraveled) * 0.04

        ClaimAmt = PerDiemAmt + MileageAmt + Bonus
        HST = ClaimAmt * HST_RATE
        TotalClaim = ClaimAmt + HST

        # Displayed Outputs
        print()
        print()
        print("                           NL Chocolate Company")
        print("                    Business Trip Travel Claim Details")
        print("    -----------------------------------------------------------------")
        EmployeeNameDsp = EmployeeFirst + " " + EmployeeLast
        print(f"    Employee Name: {EmployeeNameDsp:<32} Employee #: {EmployeeNum:>5s}")
        print()
        print(f"    Location: {TripLocation:<20}    Vehicle Owned or Rented: {VehicleUsedDsp:>6s}")
        print()
        print(
            f"    Start Date: {StartDate.strftime('%Y-%m-%d'):>10}     End Date: {EndDate.strftime('%Y-%m-%d'):>10}"
            f"      # of Days: {TravelDays:>1d}")
        print()
        print(f"    Claim Type: {ClaimTypeDsp:<9s}                  Kilometers Traveled:  {TotKmTraveled:>4}")
        print("    -----------------------------------------------------------------")
        PerDiemAmtDsp = "${:,.2f}".format(PerDiemAmt)
        print(f"                                           Per Diem Amount: {PerDiemAmtDsp:>9s}")
        if VehicleUsed == "O" or "R":
            MileageAmtDsp = "${:,.2f}".format(MileageAmt)
            print(f"                                           Mileage Amount:  {MileageAmtDsp:>9s}")
        BonusDsp = "${:,.2f}".format(Bonus)
        print(f"                                           Bonus:           {BonusDsp:>9s}")
        print("                                           --------------------------")
        ClaimAmtDsp = "${:,.2f}".format(ClaimAmt)
        print(f"                                           Claim Amount:    {ClaimAmtDsp:>9s}")
        HSTDsp = "${:,.2f}".format(HST)
        print(f"                                           HST:             {HSTDsp:>9s}")
        print()
        TotalClaimDsp = "${:,.2f}".format(TotalClaim)
        print(f"                                           Claim Total:     {TotalClaimDsp:>9s}")
        print("    -----------------------------------------------------------------")
        print()
        # Prompt for termination or continuation
        termination_value = input("     Enter 'q' to quit or any other key to continue: ")
        if termination_value.lower() == 'q':
            break

# Function to perform Option 2 from Main Menu
def InterviewQues():
    while True:
        for i in range(1, 101):
            if i % 5 == 0 and i % 8 == 0:
                print("FizzBizz")
            elif i % 5 == 0:
                print("Fizz")
            elif i % 8 == 0:
                print("Bizz")
            else:
                print(i)
        print()
        End = input("Press Enter to return to Main Menu.")
        if End == "":
            break

# Function to perform Option 3 from Main Menu
def StringsDates():
    while True:
        while True:
            allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'")
            CusFirNam = input("Enter the employee's first name: ").title()
            if CusFirNam == "":
                print("Error - Customers first name cannot be blank.")
            elif not set(CusFirNam).issubset(allowed_char):
                print("Error - Customers first name contains invalid characters.")
            else:
                break
            if CusFirNam.upper() == "End":
                print("Thank you for using our program.")
            else:
                break

        while True:
            allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-'")
            CusLasNam = input("Enter the employee's last name: ").title()
            if CusLasNam == "":
                print("Error - Customers last name cannot be blank.")
            elif not set(CusLasNam).issubset(allowed_char):
                print("Error - Customers last name contains invalid characters.")
            else:
                break

        CusNam = CusFirNam.title() + " " + CusLasNam.title()

        while True:
            allowed_numbers = set("0123456789")
            PhoneNum = input("Enter the customers phone number (7097251234): ").upper()

            if PhoneNum == "":
                print("Error - Phone number cannot be blank.")
            elif len(PhoneNum) != 10:
                print("Error- Phone number must be 10 digits.")
            elif not set(PhoneNum).issubset(allowed_numbers):
                print("Error - Phone number contains invalid characters.")
            else:
                break



        CurDate = datetime.datetime.now()
        CurDateDsp = CurDate.strftime("%Y-%m-%d")

        while True:
            allowed_numbers = set("0123456789")
            allowed_char = set("-")
            StartDate = input("Enter the start date (YYYY-MM-DD): ")

            if StartDate == "":
                print("Error - Start date cannot be blank.")
            elif not set(StartDate[0:1]).issubset(allowed_numbers):
                print("Error - Start date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(StartDate[1:2]).issubset(allowed_numbers):
                print("Error - Start date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(StartDate[2:3]).issubset(allowed_numbers):
                print("Error - Start date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(StartDate[3:4]).issubset(allowed_numbers):
                print("Error - Start date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(StartDate[4:5]).issubset(allowed_char):
                print("Error - Start date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(StartDate[5:6]).issubset(allowed_numbers):
                print("Error - Start date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(StartDate[6:7]).issubset(allowed_numbers):
                print("Error - Start date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(StartDate[7:8]).issubset(allowed_char):
                print("Error - Start date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(StartDate[8:9]).issubset(allowed_numbers):
                print("Error - Start date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(StartDate[9:10]).issubset(allowed_numbers):
                print("Error - Start date must be entered in the correct format (YYYY-MM-DD).")
            else:
                break

        while True:
            allowed_numbers = set("0123456789")
            allowed_char = set("-")
            DOB = input("Enter birth date (YYYY-MM-DD): ")

            if DOB == "":
                print("Error - Birth date cannot be blank.")
            elif not set(DOB[0:1]).issubset(allowed_numbers):
                print("Error - Birth date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(DOB[1:2]).issubset(allowed_numbers):
                print("Error - Birth date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(DOB[2:3]).issubset(allowed_numbers):
                print("Error - Birth date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(DOB[3:4]).issubset(allowed_numbers):
                print("Error - Birth date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(DOB[4:5]).issubset(allowed_char):
                print("Error - Birth date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(DOB[5:6]).issubset(allowed_numbers):
                print("Error - Birth date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(DOB[6:7]).issubset(allowed_numbers):
                print("Error - Birth date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(DOB[7:8]).issubset(allowed_char):
                print("Error - Birth date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(DOB[8:9]).issubset(allowed_numbers):
                print("Error - Birth date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(DOB[9:10]).issubset(allowed_numbers):
                print("Error - Birth date must be entered in the correct format (YYYY-MM-DD).")
            else:
                break

        while True:
            allowed_numbers = set("0123456789")
            allowed_char = set("-")
            target_date_str = input("Enter date of expected travel (YYYY-MM-DD): ")

            if target_date_str == "":
                print("Error - Travel date cannot be blank.")
            elif not set(target_date_str[0:1]).issubset(allowed_numbers):
                print("Error - Travel date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(target_date_str[1:2]).issubset(allowed_numbers):
                print("Error - Travel date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(target_date_str[2:3]).issubset(allowed_numbers):
                print("Error - Travel date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(target_date_str[3:4]).issubset(allowed_numbers):
                print("Error - Travel date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(target_date_str[4:5]).issubset(allowed_char):
                print("Error - Travel date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(target_date_str[5:6]).issubset(allowed_numbers):
                print("Error - Travel date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(target_date_str[6:7]).issubset(allowed_numbers):
                print("Error - Travel date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(target_date_str[7:8]).issubset(allowed_char):
                print("Error - Travel date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(target_date_str[8:9]).issubset(allowed_numbers):
                print("Error - Travel date must be entered in the correct format (YYYY-MM-DD).")
            elif not set(target_date_str[9:10]).issubset(allowed_numbers):
                print("Error - Travel date must be entered in the correct format (YYYY-MM-DD).")
            else:
                break

        print()
        print(f"Employee's name: {CusNam}")
        print(f"Phone number: {PhoneNum:<12s}")
        print(f"Current date: {CurDateDsp}")
        print(f"Start date: {StartDate}")
        print(f"Birth date: {DOB}")


        # Something cool: counting the number of days to a date.
        def countdown(target_date):
            while True:
                current_date = datetime.datetime.now()
                time_left = target_date - current_date

                days = time_left.days

                print(f"Time left to travel date: {days} days")
                break

        target_date = datetime.datetime.strptime(target_date_str, "%Y-%m-%d")
        countdown(target_date)

        End = input("Press Enter to return to Main Menu.")
        if End == "":
            break

def OldNew():
    while True:
        Str = "May the Force be with you."  # Defines a string variable
        Vowels = re.findall('[aeiouAEIUO]', Str)  # Finds all of the vowels within the string
        SplitVowels = ', '.join(Vowels)  # Creates a string where each vowel is separated by a comma and a space

        print("Phrase:  May the Force be with you.")  # Prints the original string
        print("Vowels: ", SplitVowels)  # Prints the separated vowels.
        print()

        End = input("Press Enter to return to Main Menu.")
        if End == "":
            break

# Main Program

while True:
    print()
    print("NL Chocolate Company")
    print("Travel Claims Processing System")
    print()
    print("1.  Enter an Employee Travel Claim.")
    print("2.  Fun Interview Question.")
    print("3.  Cool Stuff with Strings and Dates.")
    print("4.  Something Old, Something New.")
    print("5.  Quit Program.")
    print()

    try:
        Selection = int(input("     Enter choice (1-5): "))
        print()
    except:
        print("Error - Selection must be an integer (1-5).")
    else:
        if Selection == "":
            print("Error - Selection can not be blank.")
        elif Selection >= 6:
            print("Error - Selection must be between 1 and 5.")
        elif Selection <= 0:
            print("Error - Selection must be between 1 and 5.")
        elif Selection == 1:
            Output = EmpTravelClaim()
        elif Selection == 2:
            Output = InterviewQues()
        elif Selection == 3:
            Output = StringsDates()
        elif Selection == 4:
            Output = OldNew()
        elif Selection == 5:
            break