import random

options = ("rock", "paper", "scissors")
running = True
while True:
    player = None
    computer = random.choice(options)

    while player not in options:
     player = input ('Enter a choice (rock, paper, scissors): ')

    print(f'Player: {player}')
    print(f'computer: {computer}')
    if player == computer:
        print("Tie")
    elif player == "rock" and computer == "scissors":
        print('you win')
    elif player == "paper" and computer == "rock":
        print('you win!')
    elif player == "scissors" and computer == ("paper"):
        print('you win!')
    else:
        print('you lose')