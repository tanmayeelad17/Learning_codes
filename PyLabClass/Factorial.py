#find factorial of a given number using for loop
num=int(input("Enter a number:"))
fact=1
if num==0:
    print("Factorial of 0 is 1")
elif num<0:
    print("Factorial of negative number does not exist")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("Factorial of {0} is {1}".format(num,fact))

#find factorial of a given number using while loop
'count=1'
'while count<=num:'
'     fact=fact*count'
'     count=count+1'