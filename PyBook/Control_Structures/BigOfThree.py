'''Find largest of three numbers'''
a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
c=int(input("Enter value of c: "))
if a>b:
    big=a
else:
    big=b
if c>big:
    big=c
print("The largest number is: {}".format(big))
