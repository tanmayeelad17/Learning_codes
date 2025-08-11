'''Program to convert binary to decimal'''
import math
bin=int(input("Enter binary number:"))
n=bin
pos=0
dec=0
while n!=0:
    rem=n%10
    dec=dec+ int(rem*math.pow(2,pos))
    n=n//10
    pos+=1
print("{0} in decimal is {1}".format(bin,dec))