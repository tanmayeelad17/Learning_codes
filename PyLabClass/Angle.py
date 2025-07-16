#Program to accept angle value in degrees,Length  X and Y ,calculate z=xcos(A)+ysin(A)
import math
A=float(input("Enter the angle in degrees:"))
X=float(input("Enter the length X:"))
Y=float(input("Enter the length Y:"))
A1=(A*math.pi)/180  #Convert degrees to radians
print("Angle in radians is:",A1)
Z=(X*math.cos(A1))+(Y*math.sin(A1))
print("The value of Z is:",Z)