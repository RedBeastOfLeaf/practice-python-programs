# This program prints fobonacci sequence , the code uses the recursion technique


def recur_fibonacci(n):
    """Recursive function to print fibonnaci series"""
    if n <= 1:
        return n
    else:
        return (recur_fibonacci(n-1) + recur_fibonacci(n-2))    

terms = int(input("\nHow many terms do you want? :  "))
if terms <= 0:
    print("\nPlease enter a positive integer number.")
else:
    print("\nFibonnaci series: ")
    for i in range(terms):
        print(recur_fibonacci(i))
print("\n######    END    ######")
