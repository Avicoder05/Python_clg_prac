#WAP to determine sum of all positive numbers entered by user. Program continues unless user enter a negative number.

total=0
num=int(input("Enter the nummber(-ve to exit)="))
while num>0:
    total+=num
    num=int(input("Enter a number (-ve to exit)= "))
print("You are exited to negative number")
print("sum = ",total)