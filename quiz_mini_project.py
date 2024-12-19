print("Welcome to my computer Quiz!!!")
name=input("Enter your name here : ")
playing=input("Hey "+name+".... Do you want to play this game? ")
if playing.lower() != "yes":
    quit("Program Exited!!!")
else:
    print("Okay Lets Play!!!")

mark=0

answer=input("What does the CPU stands for? ")
if answer.lower()=="central processing unit":
    print("Correct answer :)")
    mark+=8
else:
    print("Incorrect answer :(")

answer=input("What does the PSU stands for? ")
if answer.lower()=="power supplying unit":
    print("Correct answer :)")
    mark+=8
else:
    print("Incorrect answer :(")

answer=input("What does the PS4 stands for? ")
if answer.lower()=="play station 4":
    print("Correct answer :)")
    mark+=8
else:
    print("Incorrect answer :(")

answer=input("What does the RAM stands for? ")
if answer.lower()=="random access memory":
    print("Correct answer :)")
    mark+=8
else:
    print("Incorrect answer :(")

answer=input("What does the OS stands for?")
if answer.lower()=="operating system":
    print("Correct answer :)")
    mark+=8
else:
    print("Incorrect answer :(")
print("You got "+str(mark)+"/40 in score and that means a percentage of ",(mark/40*100),"%")

