#WAP to find factor of given number
num=int(input("Enter number = "))
print("------------Factors of ",num,"are----------------")
for i in range (1,num+1):
   if num%i==0:
        print(i)