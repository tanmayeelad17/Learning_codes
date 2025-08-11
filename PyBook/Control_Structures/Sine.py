'''Compute sine of a given value in degrees'''
import math
x=int(input("Enter the value of x in degrees:"))
y=x
n=int(input("Enter number of terms:"))
x=x*(3.142/180.0)
temp=x
sum=x
term=x
for i in range(1,n,1):
    den=2*i*(2*i+1)
    term=-(term*x*x)/den
    sum=sum+term
print("Sin({0}) = {1}".format(y,sum))

