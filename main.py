import random as r
materials = ["rock", "paper", "scissors"]
restart = 'yes'

while restart.lower() == 'yes':
    computer_choice = r.choice(materials)
    #print("Computer chose: ", computer_choice)
    user_choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()

    if user_choice not in materials:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        continue
    print("You chose: ", user_choice)
    print("Computer chose: ", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")

    else:
        print("Computer wins!")

    restart = input('Do you want to play again?(yes or no) ').strip().lower()