# Program Description: To Do List
# Written By: Mitchell Barkley
# Written On: July 4th 2023

def AddToList():
    NewItem = input("Enter the new job for the list: ")
    ToDoList.append(NewItem)
    print()

def RemoveFromList():
    DelItem = int(input("Enter the list item to delete: "))
    ToDoList.__delitem__(DelItem - 1)

print("TO DO LIST")
ToDoList = ["Buy Maurice a Tea", "Study Essentials", "Write Python Program", "Buy the Wife some flowers"]

while True:
    JobNum = 1
    for Job in ToDoList:
        print(f"{JobNum}  {Job}")
        JobNum += 1
    print()

    print("MODIFY LIST")
    ItemNum = 1
    modifyList = ["Add Item to List", "Delete Item from List", "Exit List"]
    for Item in modifyList:
        print(f"{ItemNum}.  {Item}")
        ItemNum += 1

    changeList = int(input("What would you like to do? (select a number): "))
    if changeList == 1:
        AddToList()
    elif changeList == 2:
        RemoveFromList()
    else:
        break

'''

NumberList = []
while True:
    Number = int(input("Enter a number (-1 to end): "))
    if Number == -1:
        break

    NumberList.append(Number)

print(NumberList)

ProvList = ["NL", "NS", "PE", "NB", "QC", "MB", "SK", "AB", "ON", "BC", "YT", "NT", "NV"]
while True:
    Prov = input("Enter the Province (XX): ").upper()

    if Prov == "":
        print("Error - Province can not be blank.")
    elif len(Prov) != 2:
        print("Error - Province must only be 2 letters.")
    elif Prov not in ProvList:
        print("Error - Not a valid province.")
    else:
        break

'''