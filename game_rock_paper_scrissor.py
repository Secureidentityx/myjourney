import random

# define the options
options = ["rock", "paper", "scissors"]

while True:
    # define the player choice
    while True:
        player_choice = input("Choose rock, paper, or scissors (or type 'quit' to stop playing): ").lower()
        if player_choice == "quit":
            break
        elif player_choice in options:
            break
        else:
            print("Invalid choice. Please choose again.")

    if player_choice == "quit":
        break

    # define the computer choice
    computer_choice = random.choice(options)

    # print the choices
    print("You chose", player_choice)
    print("The computer chose", computer_choice)

    # compare the choices and determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("The computer wins!")

print("Thanks for playing!")
