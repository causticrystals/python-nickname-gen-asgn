# Nickname generator

# Import math stuff
import math
import random 

# Menu Loop
menu = True
while menu:
    #variables
    firstname = "John"
    lastname = "Doe"
    nickname_list = ["Crusher", "the Scientist", "Twinkle-Toes", "the Coder", "the Jester", "the Sloth", "Quick-Silver"]

    #print menu options
    print(f"\nMAIN MENU ({firstname} {lastname})")
    print("1. Change Name")
    print("2. Display a Random Nickname")
    print("3. Display All Nicknames")
    print("4. Add a Nickname")
    print("5. Remove a Nickname")
    print("6. Exit")

    #get input from user
    selection = input("\nSelect an option 1-6:")

    #action based on input
    if selection == "1":
        print("\nCHANGE NAME")
    elif selection == "2":
        print("\nRANDOM NICKNAME")
        r_name = random.choice(nickname_list)
        print(f"{firstname} {r_name} {lastname}")
    elif selection == "3":
        print("\nALL NICKNAMES")
    elif selection == "4":
        print("\nADD NICKNAME")
        new_nicnam = input("Please enter nickname to add:")
    elif selection == "5":
        print("\nREMOVE NICKNAME")
        nicnam_gone = input("Please enter nickname to remove:")
    elif selection == "6":
        print("Bye :-)")
        menu = False