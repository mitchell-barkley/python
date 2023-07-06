# Program Description: Menu Functions Exercise
# Written By: Mitchell Barkley
# Written On: June 7th 2023

# Import Libraries
import math
import datetime
import random

# Constants



# Program Functions
def CelciusToFahrenheit():
    Celcius = float(input("Enter a Temperature in Celcius: "))
    Fahrenheit = 9 / 5 * Celcius + 32

    FahrenheitDsp = "{:.1f}".format(Fahrenheit)
    print(f"A Temperature of {Celcius}C is {FahrenheitDsp}F")
    print()
    Wait = input("Press Enter to Continue.")


def CalculateHeartRate():
    Age = int(input("Please Enter the Age: "))
    RHR = int(input("Please Enter the Resting Heart Rate: "))

    FirstStep = 220 - Age
    SecondStep = FirstStep - RHR
    THR = SecondStep * 0.6 + RHR

    print(f"The Training Heart Rate is {THR}.")
    print()
    Wait = input("Press Enter to Continue")


def CalculateDaysUntilChristmas():
    pass


def CalculateInvoiceAge():
    CompanyName = input("Enter the Company Name: ")
    InvoiceDate = input("Enter the Invoice Date (YYYY-MM-DD): ")
    InvoiceDate = datetime.datetime.strptime(InvoiceDate, "%Y-%m-%d")
    InvoiceAmount = float(input("Enter the Invoice Amount: "))

    CurrentDate = datetime.datetime.now()
    InvoiceAge = (CurrentDate - InvoiceDate).days

    if InvoiceAge <= 30:
        Status = "OK."
    elif 31 <= InvoiceAge <= 60:
        Status = "Better think about paying."
    else:
        Status = "This one could be in trouble."

    print(f"Invoice Age:       {InvoiceAge}")
    print(f"Invoice Status:    {Status}")
    print()
    Wait = input("Press Enter to Continue")


def GuessingGame():
    while True:
        Number = random.randint(1, 100)

        NumGuess = 0
        while True:
            print()
            Guess = int(input("Enter your guess between 1 and 100: "))
            NumGuess += 1
            print()
            if Guess > Number:
                print("Your number is too high. Guess again.")
            elif Guess < Number:
                print("Your number is too low. Guess again.")
            else:
                print("Congratulations! You guessed correct!")
                print(f"You used {NumGuess} guesses.")
                break

        Choice = input("Would you like to play again? (Y/N): ").upper()
        if Choice == "N":
            break

    print()
    Wait = input("Press Enter to Continue.")
    print()




# Program Menu
while True:
    print()
    print("Maurice's quick problems - Main Menu:")
    print()
    print("1 - Convert Celcius to Fahrenheit")
    print("2 - Determine Training Heart Rate")
    print("3 - How Many Days Until Christmas")
    print("4 - How old is an Invoice")
    print("5 - Play my Guessing Game")
    print("6 - Quit")
    print()

    while True:
        try:
            Choice = int(input("Enter Choice (1-6): "))
        except:
            print("Error - Invalid entry")
        else:
            if 1 > Choice > 6:
                print("Error - Must be between 1 and 6")
            else:
                break

# Main Program
    if Choice == 1:
        CelciusToFahrenheit()
    elif Choice == 2:
        CalculateHeartRate()
    elif Choice == 3:
        CalculateDaysUntilChristmas()
    elif Choice ==4:
        CalculateInvoiceAge()
    elif Choice == 5:
        GuessingGame()
    else:
        break

print()
print("Thanks for using Maurice's Quick Problems.")
print("Please visit again soon!")
print()