'''Compute Fibonacci series using recursive function'''
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


while True:
    n=int(input("Enter number of terms:"))
    if n<=0:
        print("Enter Positive number")
    else:
        print("Fibonacci Series")
        for i in range(n):
            print(fib(i)," ",end='')
        break
