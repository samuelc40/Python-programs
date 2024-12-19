
for i in range(1, 4):
    stu_name = input("Enter student name: ")
    roll_no = int(input("Enter roll number: "))

    score1 = int(input("Score 1: "))
    score2 = int(input("Score 2: "))
    score3 = int(input("Score 3: "))

    # if score1 or score2 or score3 < 0 or score1 or score2 or score3 > 100:
    #     print("Invalid Entry!")

    if score1 + score2 + score3 >= 100 and score1 + score2 + score3 <= 300:
        print("Passed")
    else:
        print("Failed!!!")






    # elif score <= 100 and score > 50:
    #     print("passed")
    # else:
    #     print("Failed!!!")
    