'''Program to compute if a number is amstrong or not'''
num=int(input("Enter a number:"))
temp=num
sum=0
while temp!=0:
    digit=temp%10
    sum=sum+(digit*digit*digit)
    temp=temp//10
if num==sum:
    print("{} is amstrong number".format(num))
else:
    print("{} is not amstrong number".format(num))