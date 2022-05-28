import random

while True:
    user_input = input("Enter your choice: ( rock, paper or  scissors): ")
    user_input = user_input.lower()

  

    if (user_input not in ['rock', 'paper', 'scissors']):
        print ( "Please reenter the correct choice")
        continue

    computer_input = random.choice(["rock", "paper", "scissors"])

    if user_input == computer_input:
        print(f"You both selected same choice {user_input}, Game tied 👾!!!...\n")
    
    elif user_input == "rock" and computer_input == "scissors":
        print(f"{user_input} smashes {computer_input} ! You Win 🤩 🥳!!! ....\n")
    
    elif user_input == "paper" and computer_input == "rock":
        print( f"{user_input} covers {computer_input}! You Win 🤩 🥳!!!  ...\n")

    elif user_input == "scissors" and computer_input == "paper":
        print(f"{user_input} cuts {computer_input}! You win 🤩 🥳!!! ...\n")

    else:
        print ("You lose 👾👾👾!!! ...\n")

    print(f"You selected {user_input}, and your adversary chose {computer_input}. \n")
    
    go_again = input("Play again ?  (y/n): ")
    if go_again.lower() != "y":
        break


