# Program Description: Honest Harry's Car Sales Receipt with Financing Options
# Written By: Mitchell Barkley
# Written On: June 8th 2023

import datetime

# Program Constants
LICENCE_FEE_LOW = 75.00
LICENCE_FEE_HIGH = 165.00
TRANSFER_FEE_RATE = 0.01
LUX_FEE_RATE = 0.016
HST_RATE = 0.15

FINANCE_FEE = 39.99

# Program Inputs and Validations
while True:
    print()
    print("                Honest Harry Car Sales")
    print()
    print("-" * 60)
    print()
    print("Please enter the following Customer Information: ")
    print()
    while True:
        CustFirstName = input("Customer's First Name (Type END to quit): ").title()
        if CustFirstName == "":
            print("Error - Customer's First Name can not be blank.")
            print()
        else:
            break
    if CustFirstName == "End":
        break

    while True:
        CustLastName = input("Customer's Last Name: ").title()
        if CustLastName == "":
            print("Error - Customer's Last Name can not be blank.")
            print()
        else:
            break
    while True:
        CustStreet = input("Customer's Street Address: ")
        if len(CustStreet) >= 32:
            print("Error - Street Address too long - Enter Street Number and Name Only.")
            print()
        else:
            break

    while True:
        CustCity = input("Customer's City: ")
        if len(CustCity) >= 19:
            print("Error - City Name too long - Enter City Name only.")
            print()
        else:
            break

    while True:
        CustProv = input("Customer's Province (NL): ").upper()
        if len(CustProv) != 2:
            print("Error - Incorrect provincial format - Please use 2 letter input.")
            print()
        elif CustProv.isalpha() == False:
            print("Error - Invalid characters used - PLease use 2 letter input.")
            print()
        else:
            break

    while True:
        CustPostal = input("Customer's Postal Code (A1A1A1): ").upper()
        if len(CustPostal) != 6:
            print("Error - Incorrect number of characters - Please use A1A1A1 format.")
            print()
        elif CustPostal[0].isdigit():
            print("Error - Invalid character - a number was input where a letter was expected.")
            print()
        elif CustPostal[2].isdigit():
            print("Error - Invalid character - a number was input where a letter was expected.")
            print()
        elif CustPostal[4].isdigit():
            print("Error - Invalid character - a number was input where a letter was expected.")
            print()
        elif CustPostal[1].isalpha():
            print("Error - Invalid character - a letter was input where a number was expected.")
            print()
        elif CustPostal[3].isalpha():
            print("Error - Invalid character - a letter was input where a number was expected.")
            print()
        elif CustPostal[5].isalpha():
            print("Error - Invalid character - a letter was input where a number was expected.")
            print()
        else:
            break

    while True:
        CustPhone = input("Customer's Phone Number (7095551234): ")
        if CustPhone == "":
            print("Error - Phone Number can not be blank.")
            print()
        elif not CustPhone.isdigit():
            print("Error - Number entered contains invalid characters.")
            print()
        elif len(CustPhone) != 10:
            print("Error - Phone Number must be 10 digits. (7095551234)")
            print()
        else:
            break

    while True:
        PlateNum = input("Licence Plate Number (XXX999): ").upper()
        if PlateNum == "":
            print("Error - Licence Plate Number can not be blank (XXX999).")
            print()
        elif len(PlateNum) != 6:
            print("Licence Plate Number must be 6 characters. (XXX999)")
            print()
        elif PlateNum[0:3].isalpha() == False:
            print("Error - First three characters must be letters. (XXX999)")
            print()
        elif PlateNum[3:].isdigit() == False:
            print("Error - Last three characters must be numbers. (XXX999)")
            print()
        else:
            break

    CarMake = input("Make of the Car: ")
    CarModel = input("Model of the Car: ")

    while True:
        CarYear = input("Year of the Car: ")
        if len(CarYear) != 4:
            print("Error - Year entered is not valid.")
            print()
        elif CarYear.isdigit() == False:
            print("Error - Year entered contains invalid character(s).")
            print()
        else:
            break

    while True:
        try:
            while True:
                SalePrice = float(input("Sale Price: "))
                if SalePrice > 50000:
                    print("Error - Sale Price can not exceed $50,000.00.")
                    print()
                elif SalePrice < 0:
                    print("Error - Sale Price can not be negative.")
                    print()
                else:
                    break
        except:
            print("Error - Invalid Sale Price.")
            print()
        else:
            break

    while True:
        try:
            while True:
                TradePrice = float(input("Trade-in Value: "))
                if TradePrice >= SalePrice:
                    print("Error - Trade-in Value can not exceed Sale Price.")
                    print()
                else:
                    break
        except:
            print("Error - Invalid Trade-in Value.")
            print()
        else:
            break



    EmpName = input("Name of Salesperson: ")
    print()
    print()

    InvoiceDate = datetime.datetime.now()
    InvoiceDateDsp = InvoiceDate.strftime("%B %d, %Y")

    FinanceDateDsp = InvoiceDate.strftime("%d-%b-%Y")
    FirstPay = InvoiceDate + datetime.timedelta(days = 30)
    FirstPayDsp = FirstPay.strftime("%d-%b-%Y")

# Program Calculations

    PriceAfterTrade = SalePrice - TradePrice

    TransferFee = SalePrice + TRANSFER_FEE_RATE

    if SalePrice <= 5000:
        LicenceFee = LICENCE_FEE_LOW
        SubTotal = PriceAfterTrade + LICENCE_FEE_LOW + TransferFee
    else:
        LicenceFee = LICENCE_FEE_HIGH
        SubTotal = PriceAfterTrade + LICENCE_FEE_HIGH + TransferFee

    if SalePrice > 20000:
        LuxTax = SalePrice * LUX_FEE_RATE
    else:
        LuxTax = 0

    HST = SubTotal * HST_RATE

    TotalSalePrice = SubTotal + HST

    ReceiptNum = CustFirstName[0] + CustLastName[0] + "-" + PlateNum[3:] + "-" + CustPhone[6:]

# Display Formatting
    SalePriceDsp = f"${SalePrice:,.2f}"
    TradePriceDsp = f"${TradePrice:,.2f}"
    PriceAfterTradeDsp = f"${PriceAfterTrade:,.2f}"
    LicenceFeeDsp = f"${LicenceFee:,.2f}"
    TransferFeeDsp = f"${TransferFee:,.2f}"
    SubTotalDsp = f"${SubTotal:,.2f}"
    HSTDsp = f"${HST:,.2f}"
    TotalSalePriceDsp = f"${TotalSalePrice:,.2f}"

# Program Output

    print(f"Honest Harry Car Sales                          Invoice Date: {InvoiceDateDsp:>15s}")
    print(f"Used Car Sale and Receipt                       Receipt No:       {ReceiptNum:>11s}")
    print()
    print(f"                                          Sale Price:              {SalePriceDsp:>10s}")
    print(f"Sold to:                                  Trade Allowance:         {TradePriceDsp:>10s}")
    print(f" "*41, "-"*35)
    print(f"      {CustFirstName[0]}. {CustLastName:<28s}     Price after Trade:       {PriceAfterTradeDsp:>10s}")
    print(f"      {CustStreet:<33s}   Licence Fee:             {LicenceFeeDsp:>10s}")
    print(f"      {CustCity:<20s},{CustProv:<2s} {CustPostal:<6s}      Transfer Fee:            {TransferFeeDsp:>10s}")
    print(f" "*41, "-"*35)
    print(f"Car Details:                              Subtotal:                {SubTotalDsp:>10s}")
    print(f"                                          HST:                     {HSTDsp:>10s}")
    print(f"      {CarYear:<4s} {CarMake:<13s} {CarModel:<10s}      -----------------------------------")
    print(f" "*41, f"Total sales price:       {TotalSalePriceDsp:>10s}")
    print(f"-"*77)
    print(f" "*17, "Best used cars at the best price!")
    print()
    print()
    print()
    print(f" "*30, "Financing     Total        Monthly")
    print(f"    # Years    # Payments         Fee        Price        Payment")
    print(f"    -------------------------------------------------------------")

    Year = 1
    for Year in range(1, 5):
        NumPayment = Year * 12
        FinanceFee = Year * FINANCE_FEE
        TotalPrice = TotalSalePrice + FinanceFee
        MonthlyPayment = TotalPrice / NumPayment

        FinanceFeeDsp = f"${FinanceFee:,.2f}"
        TotalPriceDsp = f"${TotalPrice:,.2f}"
        MonthlyPaymentDsp = f"${MonthlyPayment:,.2f}"

        print(f"       {Year:<1d}            {NumPayment:<3d}     {FinanceFeeDsp:>10s}    {TotalPriceDsp:>10s}   {MonthlyPaymentDsp:>10s}")

        Year += 1

    print(f"    -------------------------------------------------------------")
    print(f"    Invoice Date: {FinanceDateDsp:<9s}     First payment date: {FirstPayDsp}")
    print()
