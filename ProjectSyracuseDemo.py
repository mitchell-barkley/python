# Program Description: Syracuse Problem
# Written By: Mitchell Barkley
# Written On: June 25th 2023

# Libraries
import random

# Main
n = random.randint(1, 101)
print(n)
for num in range(1, 200):
    if n % 2 == 0:
        n = n / 2
    elif n % 2 == 1:
        n = n * 3 + 1
    print(n)
