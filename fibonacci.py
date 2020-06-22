# this programme prints the fibonnaci series

number = int(input("Enter the count of numbers you want: "))
f1 = f2 = 1
print(f1, f2, end=' ')

i = 2
while i < number:
    f1, f2 = f2, f1+f2
    print(f2, end=' ')
    i += 1
print()    

