import random

def rps(computer, player):
    if player == computer:
        print("Tie")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("Player wins")
    else:
        print("Computer wins")
def play_game():
    options = ("rock", "paper", "scissors")
    running = True

    while running:
        player = None
        computer = random.choice(options)

        while player not in options:
            player = input('Enter a choice (rock, paper, scissors): ')

        print(f'Player: {player}')
        print(f'Computer: {computer}')

        rps(computer, player)
        break
play_game()

