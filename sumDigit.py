#WAP to calculate sum of digit of an integer between 1 to 1000
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Input: an integer between 1 and 100
number = int(input("Enter an integer between 1 and 100: "))

if 1 <= number <= 100:
    result = sum_of_digits(number)
    print(f"The sum of the digits of {number} is {result}.")
else:
    print("Please enter a valid integer between 1 and 100.")

print(sum)