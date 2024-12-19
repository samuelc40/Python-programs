print("Grades are computed using a weighted average of test counts 70%, lab exams 20%, assignments 10%")
print("Enter the Score by the student")
W = int(input("Written Test: "))
L = int(input("Lab Exam: "))
A = int(input("Assignments: "))

oversall = (W * 70)/100 + (L * 20)/100 + (A * 10)/100

print("Grade scored by the student during this academic year is: ",oversall,"%")