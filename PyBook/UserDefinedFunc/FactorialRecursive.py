'''To calculate factorial using User defined function(Recusive)'''
def fact(n):
    if n==1:
        return 1
    else:
        result=n*fact(n-1)
        return result
n=int(input("Enter a number:"))
print("Factorial of ",n,"is:",fact(n))