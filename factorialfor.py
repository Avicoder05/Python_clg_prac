factorial =1
n=int (input("enter number whose factorial you want = "))
for i in range(2,n+1):
    factorial*=i
print("factorial of number ",n,"=",factorial)