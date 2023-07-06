# Program Description: Basic Bank Machine
# Written By: Mitchell Barkley
# Written On: May 17th 2023

print()
print("WELCOME TO THE BANK OF NEWFOUNDLAND")
print()
print("*"*60)
print()

# Input
CurrentBalance = float(input("Please enter the current account balance: "))
print()
# Choice between deposit or withdrawal
TransType = input("Please choose the transaction type (D - Deposit or W - Withdrawal): ").upper()
print()
if TransType == "D":
    TransAmount = float(input("Please enter the deposit amount: "))
    NewBalance = CurrentBalance + TransAmount
    Type = "Deposit"
elif TransType == "W":
    TransAmount = float(input("Please enter the withdrawal amount: "))
    if CurrentBalance > TransAmount:
        NewBalance = CurrentBalance - TransAmount
        Type = "Withdrawal"
    else:
        print("Insufficient Funds")
        TransAmount = 0
        NewBalance = CurrentBalance
        Type = "NSF"
else:
    print("Error Detected")
    TransAmount = 0
    NewBalance = CurrentBalance
    Type = "Error"

TransTypeDsp = Type
print()
print(f"Transaction Type:          {TransTypeDsp:<9s}")
print()
TransAmountDsp = f"${TransAmount:,.2f}"
print(f"Transaction Amount:        {TransAmountDsp:<9s}")
NewBalanceDsp = f"${NewBalance:,.2f}"
print(f"New Balance:               {NewBalanceDsp:<9s}")
print()
print("-"*60)
