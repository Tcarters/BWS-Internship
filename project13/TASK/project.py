#!/usr/bin/python3

# 1. Ask for user input
# 2. Create a dynamic URL based on step 1
# 3. Fetch the data from the url in step 2
# 4. Convert JSON to a dictionary
# 5 Print out pokemon data

import requests


while True:
    user_input =  int( input("Please enter  the Pokemon Id from '1 to 20' : ") )
    
    if user_input in range(1, 21):
        print( f"You entered Pokemon id:  { user_input } ")
                
        req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{user_input}")

        if  req.status_code == 200:
            base_url = req.json()


            choices = ['base_experience' , 'height', 'name', 'species', 'weight', 'abilities'  ]
            user_choice = input(f"Please select following items {choices} :")
           
            if user_choice in choices:
                if user_choice == 'abilities':
                    print("Abilities:  \n")
                    for a in base_url['abilities']:
                        print("User abilities: \t\t", a['ability'], '\n\t')
                else:
                    print (f"\nGot, {user_choice}: \t", base_url.get( f'{user_choice}', None), '\n\n' )
            
            else:
                print("\nUnknown data entered !!! Try again after ....\n")
        
        else:
            print (" \n Unable to connect to the site !!! Try again...")


    elif user_input not in range(1, 21):
        user_input = int( input("Please reenter your number from this range [1..20] :") )

    
    print ( "One second wait ...")

    end_game = input ( "What to continue ? [y/n] : ")
    if end_game == 'y':
        continue

    break

