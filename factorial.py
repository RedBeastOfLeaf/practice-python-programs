# This program prints the factorial of the provided integer


def recur_factorial(n):
    """This prints the factorial of a given number"""
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)

number = int(input("Enter the number: "))
if number < 0:
    print("\nFactorial of negative number does not exist.")
elif number == 0:
    print("\nThe factorial of 0 is 1")
else:
    print("]\nThe factorial of",number,"is",recur_factorial(number))
