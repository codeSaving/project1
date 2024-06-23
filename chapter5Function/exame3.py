import random


def rps(computer_choice, player_choice):
    if computer_choice == player_choice:
        print("Tie")
        return "Tie"
    elif (computer_choice == "rock" and player_choice == "scissors") or \
            (computer_choice == "scissors" and player_choice == "paper") or \
            (computer_choice == "paper" and player_choice == "rock"):
        print("Computer wins")
        return "Computer wins"
    else:
        print("Player wins")
        return "Player wins"


def play_game():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    while True:
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if player_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        print(f"Computer's choice: {computer_choice}")
        result = rps(computer_choice, player_choice)
        if result != "Tie":
            break
        else:
            print("It's a tie. Play again.")
            computer_choice = random.choice(choices)


# Start the game
play_game()
