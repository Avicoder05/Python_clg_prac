#WAP to calculate sum of digit of an integer between 1 to 1000


number=int(input("Enter number = "))
digit1=number//100
remainder1=(number%100)
digit2=remainder1//10
digit3=remainder1%10
sum = digit1+digit2+digit3
print("The number whose digits need to be summed is : ",number)
print("Sum of digit of given number is : ",sum)