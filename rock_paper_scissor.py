import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissor"]

while True:
    if user_wins == 5 or computer_wins == 5:
        break
    user_input = input("Type Rock / Paper / Scissor or Q to quit: ").lower()
    if user_input == "q":
        quit("Game Exited")

    if user_input not in options:
        print("That's not an option!")
        continue

    random_number = random.randint(0, 2)
    # Rock: 0, Paper: 1,Scissor:2

    computer_pick = options[random_number]
    print("Computer Picked",computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You win...!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You win...!")
        user_wins += 1
        continue

    elif user_input == "scissor" and computer_pick == "paper":
        print("You win...!")
        user_wins += 1
        continue
    elif user_input == computer_pick:
        print("You both picked ", computer_pick + ", So drow...")
        continue

    else:
        print("You lost...!")
        computer_wins += 1
        continue

print()

print("Computer score: ", computer_wins)
print("Your score: ", user_wins)

if user_wins > computer_wins:
    print("Congrats.....You won!!!")
else:
    print("Oops....You lose!!!")


