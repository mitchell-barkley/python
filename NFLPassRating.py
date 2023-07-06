# Program Description: NFL Pass / Rush Rating
# Written By: Mitchell Barkley
# Written On: May 16th 2023

# User Inputs
print("St. John's Pebbles Football Team")
print("Game Statistics Program")
print()
print("Please enter the following required values:")
print()
DateOfGame = input("Game Date (yyyy-mm-dd): ")
Opponent = input("Opponent: ")
Location = input("Enter The Location Of The Game: ")
FinalScore = input("Enter The Final Score Of The Game: ")

PassAttempts = int(input("Number Of Pass Attempts: "))
PassComplete = int(input("Number Of Completed Passes: "))
TotalPassYards = int(input("Total Passing Yards: "))
TouchDownPass = int(input("Number Of Passing Touchdowns: "))
InterceptPass = int(input("Number Of Intercepted Passes: "))
print()
RushAttempts = int(input("Number Of Rush Attempts: "))
TotalRushYards = int(input("Total Rushing Yards: "))
TouchDownRush = int(input("Number Of Rushing Touchdowns: "))
print()

# Calculations
PassPercent = (PassComplete / PassAttempts) * 100
YardsPerPass = (TotalPassYards / PassComplete)

TotalTouchDown = TouchDownPass + TouchDownRush
TotalAttempts = PassAttempts + RushAttempts

Formula1 = (PassPercent - 0.3) * 5
Formula2 = ((TotalPassYards / PassAttempts) - 3) * 0.25
Formula3 = (TouchDownPass / PassAttempts) * 20
Formula4 = 2.375 - ((InterceptPass / PassAttempts) * 25)

PassRating = (Formula1 + Formula2 + Formula3 + Formula4)

RushYardsAverage = TotalRushYards /RushAttempts
TouchDownEfficiency = (TouchDownRush / RushAttempts) * 100

# Outputs
print("St. John's Pebbles Football Team")
print("Game Statistics Program")
print()
print(f"Game Statistics vs {Opponent:<22s}     on {DateOfGame:>10s}")
print("-"*60)
print("Quarterback Statistics:")
print()
PassPercentDsp = f"{PassPercent:.2f}%"
print(f"Number of Pass Attempts:  {PassAttempts:>3d}    Pass Completion %:   {PassPercentDsp:>3s}")
print(f"Number of Completions:    {PassComplete:>3d}")
YardsPerPassDsp = f"{YardsPerPass:.2f}"
print(f"Total Passing Yards:      {TotalPassYards:>3d}    Yards Per Pass:       {YardsPerPassDsp:>3s}")
print(f"Number of Touchdowns:     {TouchDownPass:>3d}")
PassRatingDsp = f"{PassRating:.1f}"
print(f"Number of Interceptions:  {InterceptPass:>3d}    NFL Passer Rating:    {PassRatingDsp:>4s}")
print()
print("Rushing Statistics:")
print()
RushYardsAverageDsp = f"{RushYardsAverage:.1f}"
print(f"Number of Rushing Atts:   {RushAttempts:>3d}    Avg Yards Per Rush:    {RushYardsAverageDsp:>3s}")
print(f"Total Rushing Yards:      {TotalRushYards:>3d}")
TouchDownEfficiencyDsp = f"{TouchDownEfficiency:.1f}%"
print(f"Number of Rushing TD's:   {TouchDownRush:>3d}    TD Efficiency:         {TouchDownEfficiencyDsp:>3s}")
print("-"*60)