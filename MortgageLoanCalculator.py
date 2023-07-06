# Program Description: Mortgage Loan Payment Calculator
# Written By: Mitchell Barkley
# Written On: May 24th 2023

# Constants
INTEREST_RATE = 0.065

# Program Inputs
while True:

    LoanAmount = float(input("Enter the amount of the loan: "))
    Reason = input("Loan purpose: ")

    # Program Calculations
    print()
    LoanAmountDsp = f"${LoanAmount:,.2f}"
    print(f"  Loan Options for 10 years on {LoanAmountDsp:<9s}")
    print()
    print(" Years     Interest   Total Amount    Monthly Payment")
    print("-"*52)

    for Years in range(1, 11):
        Interest = LoanAmount * INTEREST_RATE * Years
        TotalAmount = LoanAmount + Interest
        MonthlyPayment = TotalAmount / (Years * 12)

        InterestDsp = f"${Interest:,.2f}"
        TotalAmountDsp = f"${TotalAmount:,.2f}"
        MonthlyPaymentDsp = f"${MonthlyPayment:,.2f}"

        print(f"  {Years:>2d}    {InterestDsp:>11s}    {TotalAmountDsp:>11s}    {MonthlyPaymentDsp:>10s}")
    print("-"*52)
    print()
    Continue = input("Do you want to process another loan? (Y/N): ").upper()
    if Continue == "N":
        print()
        break