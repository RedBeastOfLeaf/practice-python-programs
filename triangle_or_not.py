# This calculates whether the given sides of a tringle exist or not
print("\nProvide the lenght of the sides of the triangle: ")
a = float(input("\nfirst side = "))
b = float(input("second side = "))
c = float(input("third side = "))

if a+b>c and a+c>b and b+c>a:
    print("\nThe triangle exists.")
else:
    print("\nThe triangle does not exixts. ")    
