'''Program to print Fibonacci series up to n terms'''
num=int(input("enter a integer number:"))
fib0=0
fib1=1
i=0
while i<num:
    if i<=1:
        fibnext=i
    else:
        fibnext=fib0+fib1
        fib0=fib1
        fib1=fibnext
    print("fib{0}={1}".format(i+1,fibnext))
    i=i+1
    