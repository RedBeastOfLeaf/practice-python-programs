# To check whether a number is palindrome or not

n= int(input("Enter the number : "))
reverse = 0
number = n
#reversing the given number
while(n != 0):
  remainder = n % 10
  reverse = reverse * 10 + remainder
  n = int(n / 10)
if(number == reverse):
  print("\nThe number is a Palindrome")
else:
  print("\nThe number is Not a Palindrome")
