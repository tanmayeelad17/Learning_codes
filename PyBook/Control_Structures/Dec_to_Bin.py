'''program to convert decimal number to its corresponding binary number'''
dec=int(input("Enter a decimal num:"))
n=dec
bin=0
pos=1
while n!=0:
    rem=n%2
    bin=bin+ (rem*pos)
    n=n//2
    pos=pos*10
print("{0} in binary number is {1}".format(dec,bin))