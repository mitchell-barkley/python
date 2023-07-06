# Program Description: Manipulating Strings Exercise
# Written By: Mitchell Barkley
# Written On: May 31st 2023

Title = "mr."
CustFirst = "john"
CustLast = "doe"

FullName = (Title + " " + CustFirst + " " + CustLast).title()
print(FullName)

FullName = (CustFirst[0] + ". " + CustLast).title()
print(FullName)

FullName = (Title + " " + CustFirst[0] + ". " + CustLast).title()
print(FullName)

FullName = (CustLast + ", " + CustFirst[0] + ".").title()
print(FullName)

FullName = (CustLast + ", " + CustFirst[0]).title()
print(FullName)

DeptName = "information technology".title()
print(DeptName)

CurrDate = "2023-05-31"
CustFirst = "John"
CustLast = "Doe"
LocCode = "AJRD".upper()
TransCode = 14974
CustCtr = 4768

TrackNo = CustFirst[0] + CustLast[0] + "-" + LocCode[0:2] + "-" + str(TransCode)[3:5] + "-" + CurrDate[0:4] + str(CustCtr)
print(TrackNo)

print(f"My name is {FullName}")

print(f"My name is {CustFirst:<15s} {CustLast:<15s}.")

'''
Prov = input("Enter the Province (NL): ").upper()
print(Prov)
CustFirst = input("Enter the Customer's First Name: ")
print(CustFirst)
CustFirst = input("Enter the Customer's First Name: ").lower()
print(CustFirst)
CustFirst = input("Enter the Customer's First Name: ").title()
print(CustFirst)
CustFirst = input("Enter the Customer's First Name: ").capitalize()
print(CustFirst)
'''

while True:
    PhoneNum = "5197347119"
    '''PhoneNum = input("Enter the Phone Number (7777777777): ")'''
    if PhoneNum == "":
        print("Error - Phone Number can not be blank.")
    elif len(PhoneNum) != 10:
        print("Error - Phone Number is not valid.")
    elif not PhoneNum.isdigit():
        print("Error - Phone Number must be 10 digits.")
    else:
        break

PhoneNum = "(" + PhoneNum[0:3] + ") " + PhoneNum[3:6] + "-" + PhoneNum[6:]
print(PhoneNum)
print()

while True:
    CardNum = "5234567891234567"
    '''CardNum = input("Enter the Credit Card Number (9999999999999999): ")'''
    if CardNum == "":
        print("Error - Card Number can not be blank.")
    elif len(CardNum) != 16:
        print("Error - Card Number must be 16 digits.")
    elif not CardNum.isdigit():
        print("Error - Card number must be 16 digits.")
    elif CardNum[0] != "4" and CardNum[0] != "5":
        print("Error - Unknown card type.")
    else:
        break

if CardNum[0] == "4":
    print("Visa")
elif CardNum[0] == "5":
    print("MasterCard")
else:
    print("Other")

CardNum = CardNum[0:4] + " " + CardNum[4:8] + " " + CardNum[8:12] + " " + CardNum[12:]
print(CardNum)
print()


while True:

    '''LicenceNum = input("Enter the Licence Number (ABC123): ").upper()'''
    LicenceNum = "abc123".upper()

    if LicenceNum == "":
        print("Error - Licence can not be blank.")
    elif len(LicenceNum) != 6:
        print("Error - Licence must be 6 characters. (ABC123)")
    elif LicenceNum[3:].isdigit() == False or LicenceNum[0:3].isalpha() == False:
        print("Error - Invalid Licence (Check Provincial Input).")
    else:
        break

print(LicenceNum[0:3] + " " + LicenceNum[3:])
print()

while True:

    '''PostalCode = input("Enter the Postal Code (A1A1A1): ").upper()'''
    PostalCode = "a2a2a2".upper()
    if PostalCode == "":
        print("Error - Postal Code can not be blank.")
    elif len(PostalCode) != 6:
        print("Error - Postal Code must be 6 characters. (A3A3A3)")
    elif PostalCode[0].isdigit() or PostalCode[1].isalpha() or PostalCode[2].isdigit() or PostalCode[3].isalpha() or PostalCode[4].isdigit() or PostalCode[5].isalpha():
        print("Error - Invalid Postal Code.")
    else:
        break
print(PostalCode[0:3] + " " + PostalCode[3:])
print()


while True:
    '''Province = input("Enter the Province (ON): ").upper()'''
    Province = "ON"
    if Province == "":
        print("Error - Province can not be blank.")
    elif len(Province) != 2:
        print("Error - Province is invalid.")
    elif Province != "AB" and Province != "BC" and Province != "NL" and Province != "PE" and Province != "NB" and Province != "QC" and Province != "ON" and Province != "NT" and Province != "NU" and Province != "YT":
        print("Error - Not a valid Province")
    else:
        break
print(Province)
print()

while True:
    allowed_char = set("abcdefghijklmnopqrstuvwxyz")
    allowed_CHAR = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    allowed_Num = set("1234567890")
    allowed_sym = set("!@#$%^&*")
    Password = input("Enter your new password: ")

    NumUpper = 0
    NumLower = 0
    NumNum = 0
    NumSpec = 0

    for Char in Password:
        if set(Char).issubset(allowed_CHAR):
            NumUpper += 1
        elif set(Char).issubset(allowed_char):
            NumLower += 1
        elif set(Char).issubset(allowed_Num):
            NumNum += 1
        elif set(Char).issubset(allowed_sym):
            NumSpec += 1



    if len(Password) <= 7:
        print("Error - Password must be at least 7 characters.")
    elif NumUpper == 0 or NumLower == 0 or NumNum == 0 or NumSpec ==0:
        print(f"Error # - {NumUpper}{NumLower}{NumNum}{NumSpec}")
        print("Password must contain at least 1 uppercase, 1 lowercase, 1 number and 1 special character.")
    else:
        break

print("New password accepted.")
