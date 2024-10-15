# Program to enter a day of week as integer, like 1 for monday,2 for tuesday and so on and determine whether it's holiday or not
day = int(input("Enter day of week(1 for monday .....) = "))
if day == 7:
    print("today is holiday")
else:
    print("today is not holiday")