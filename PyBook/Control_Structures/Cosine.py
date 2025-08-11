'''Program to compute cosine of a value(degrees) using maclaurin series of cos'''
import math
a=int(input("Enter the value of x in degrees:"))
n=int(input("Enter number of terms:"))
x=a*(math.pi)/180    #Convert degrees to radians
sum=1
sign=-1
for i in range(2,n,2):
    fact=1
    for j in range(i,0,-1):
        fact=fact*j
    sum=sum+ (math.pow(x,i)/(sign*fact))
    sign=sign*(-1)
print("Cos{0}= {1}".format(a,sum))