'''Calculate area of triangle when 3 sides are given'''
import math
print("Enter the 3 sides")
a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle is:",area)