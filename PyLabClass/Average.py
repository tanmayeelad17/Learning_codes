#Program to find average of 1st n natural numbers

n=int(input("Enter a number:"))
num=n
sum=0
if n<=0:
    print("Enter a number greater than 0")
else:
    while n>0:                   
        sum=sum+n
        n=n-1
    print("Sum =",sum)
    avg=sum/num
    print("Average=",avg)

'''for i in range(1,n+1):
        sum+=i
    print("sum=",sum)
    avg=sum/num
    print("avg=",avg)'''