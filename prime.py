#WAP to check prime
i=1
factor=0#count number of factor
num=int(input("enter a number = "))
while i<num:
    if num%i==0: #dividing number by 1,2,.....num
        factor+=1
    i+=1
if factor ==2:
    print(num,"is prime")
else:
    print(num,"is not prime")