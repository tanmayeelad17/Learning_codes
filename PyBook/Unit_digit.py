'''Program to print ones place of any given integer'''
n=int(input("Enter a integer:"))
temp=n
unit_place=(temp%10)
print("The unit digit of {0} is:{1}".format(n,unit_place))
