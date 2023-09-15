# Nickname generator

# Import random stuff
import random 

#variables
firstname = "John"
lastname = "Doe"
nickname_list = ['Crusher', 'the Scientist', 'Twinkle-Toes', 'the Coder', 'the Jester', 'the Sloth', 'Quick-Silver']

# Menu Loop
menu = True
while menu:

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
    if selection == "1": #change name
        print("\nCHANGE NAME")
        firstname = input("Please enter first name: ")
        lastname = input("Please enter last name: ")
        print(f"name has been changed to: {firstname} {lastname}")
    elif selection == "2": #random name
        print("\nRANDOM NICKNAME") 
        r_name = random.choice(nickname_list)
        print(f'{firstname} "{r_name}" {lastname}')
    elif selection == "3": #all names
        for x in nickname_list:
            print(f'{firstname} "{x}" {lastname}')
    elif selection == "4": #add name
        print("\nADD NICKNAME")
        new_nicnam = input("Please enter nickname to add: ")
        #test input
        if new_nicnam in nickname_list:
            print(f"{new_nicnam} is already in the list!")
        else:
            nickname_list.append(new_nicnam)
            print(f"{new_nicnam} is now in the list :-D!")
    elif selection == "5": #remove name
        print("\nREMOVE NICKNAME")
        nicnam_gone = input("Please enter nickname to remove:")
        #test input
        if nicnam_gone in nickname_list:
            nickname_list.remove(nicnam_gone)
            print(f'{nicnam_gone} removed from list, bye forever "{nicnam_gone}"!!')
        else:
            print(f"{nicnam_gone} was not found in nickname list sorry :-(")
    elif selection == "6": #exit loop
        print("Bye :-)")
        menu = False