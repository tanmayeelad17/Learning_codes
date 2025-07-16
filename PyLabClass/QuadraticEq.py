#Find roots of a Quadratic equation ax^2+bx+c=0
import math
import cmath #for complex numbers
print("Enter coefficient values a,b,c")
a=float(input("Enter a:"))
if a!=0:
    b=float(input("Enter b:"))
    c=float(input("Enter c:"))
    d=b*b-4*a*c
    if d>0:
        root1=(-b+math.sqrt(d))/(2*a)
        root2=(-b-math.sqrt(d))/(2*a)
        print("Roots are real and distinct")
        print("Root1=",root1, "Root2=",root2)
    elif d==0:
        root1=root2=-b/(2*a)
        print("Roots are equal")
        print("Root1=Root2=",root1)
    else:
        real=-b/(2*a)
        imaginery=cmath.sqrt(d)/(2*a)
        print("roots are imaginery")
        print("Root1=",real+imaginery, "Root2=",real-imaginery)
else:
    print("if a=0 equation is not quadratic")

