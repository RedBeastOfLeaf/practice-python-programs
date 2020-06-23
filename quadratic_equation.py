import cmath
print("First transform your equation and give values of a,b,c respectively in order")
a = float(input("\nEnter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
d = (b**2) - (4*a*c)
root1 = (-b-cmath.sqrt(d)/(2*a))
root2 = (-b+cmath.sqrt(d)/(2*a))
if(d > 0):
    print("\nThe roots are real and positive.")
    print("The first root is : " +str(root1))
    print("The second root is : " +str(root2))
elif(d < 0):
    print("\nThe roots are imaginary and negative.")    
    print("The first root is : " +str(root1))
    print("The second root is : " +str(root2))
    

