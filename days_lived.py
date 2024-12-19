import datetime

live = datetime.datetime.now()

print("Today: ",live.strftime("%d/%m/%y"))

print("Enter your date birth ")

x = datetime.datetime(day=int(input("Day: ")),month=int(input("Month: ")),year=int(input("Year: ")))
y = live
diff = y-x

print("You lived ",diff)