#Find the sum of even or odd numbers upto the number enterd by the user

n=int(input("Enter a number:"))


def evenodd(n):
    esum=0
    osum=0
    if n%2==0:
        print("The number is even")
        for i in range(0,n+1,2):
            esum=esum+i
        print("Sum of even nos=",esum)
    else:
        print("The number is odd")
        for i in range(1,n+1,2):
            osum=osum+i
        print("Sum of odd numbers=",osum)

evenodd(n)