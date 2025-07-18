'''Program to swap two variables without using the third variable'''
print("Program to swapp two variables")
m=int(input("Enter value of m:"))
n=int(input("Enter value of n:"))
print("Values before swapping m:{0} n:{1}".format(m,n))
m=m+n
n=m-n
m=m-n
print("Value after swapping m={0} n={1}".format(m,n))
