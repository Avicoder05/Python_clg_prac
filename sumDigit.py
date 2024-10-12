#WAP to calculate sum of digit of an integer between 1 to 1000
number = 566
digit1=number//100
remainder1=(number%100)
digit2=remainder1//10
digit3=remainder1%10
sum = digit1+digit2+digit3
print(sum)