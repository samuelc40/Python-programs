import random

top_of_range = input("Type a number : ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Type a number greater than Zero next time...")
        quit("Program Exited!!!")
else:
    print("Type a number next time...")
    quit("Program Exited!!!")

r = random.randrange(0, top_of_range)

guesses=0

while True:
    guesses+=1
    user_guess = input("Make a guess : ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Type a number next time...")
        continue

    if user_guess == r:
        print("You got it correct $$$")
        break

    elif user_guess > r:
        print("You were above the number... ")

    else:
        print("You were below the number...")

if guesses == 1:
    print("You got it in first try!!!.....Congrats!!!")
else:
    print("You got the right number in",guesses,"Guesses...")
