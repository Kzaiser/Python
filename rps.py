import random

user_wins = 0
computer_wins = 0

rps = ["rock", "paper", "scissors"]

while user_wins != 2 and computer_wins != 2:
    user_input = input("Type Rock/Paper/Scissors or Q to quit, best 2/3: ").lower()
    if user_input == 'q':
        break
    
    if user_input not in rps:
        continue

    random_number = random.randint(0, 2)
    # rock = 0, paper = 1, scissors = 2

    computer_pick = rps[random_number]
    print("Computer picked: ", computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("W")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("W")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("W")
        user_wins += 1
    elif user_input == computer_pick:
        print("Tie")
    else:
        print("You lost")
        computer_wins += 1
        
print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")