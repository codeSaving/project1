import random


def rps(computer_score, player_score):
    if computer_score > player_score:
        print("Computer wins")
    elif player_score > computer_score:
        print("Player wins")
    else:
        print("Tie")


def play_game():
    options = ("rock", "paper", "scissors")
    player_score = 0
    computer_score = 0

    while True:
        computer_number = random.randint(1, 3)
        if computer_number == 1:
            computer = "rock"
        elif computer_number == 2:
            computer = "paper"
        else:
            computer = "scissors"

        player = None

        while player not in options:
            player = input('Enter a choice (rock, paper, scissors): ').lower()

        print(f'Player: {player}')
        print(f'Computer: {computer}')

        if player == computer:
            print("It's a tie! Play again.")
        elif (player == "rock" and computer == "scissors") or \
                (player == "paper" and computer == "rock") or \
                (player == "scissors" and computer == "paper"):
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            computer_score += 1

        rps(computer_score, player_score)

        # Ask the player if they want to play another round
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    return computer_score, player_score


# Start the game and capture the final scores
final_computer_score, final_player_score = play_game()
print(f'Final Scores - Computer: {final_computer_score}, Player: {final_player_score}')
