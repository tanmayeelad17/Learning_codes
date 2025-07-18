'''Python program to demonstrate built-in mathematical functions supported in math module'''
import math
x=25
print("Square root of" ,x,"is:",math.sqrt(x))
x=4
y=2
print("Power of",x,"raised to",y,"is:",math.pow(x,y))
x=6
print("The log of",x,"base 10 is:",math.log10(x))
print("Value of pi is:",math.pi)
print("Value of e is:",math.e)
x=3.14978
print("The ceil value(smallest int value greater than or equal to {}".format(x),"):",math.ceil(x))
x=-3.14978
print("The absolute value of {0} is:{1}".format(x,math.fabs(x)))
x=6
print("Factorial of {0} is:{1}".format(x,math.factorial(x)))
x=45
print("Sin of {0} degrees :{1}".format(x,math.sin(math.radians(x))))
print("Cos of {0} degrees :{1}".format(x,math.cos(math.radians(x))))
print("Tan of {0} degrees :{1}".format(x,math.tan(math.radians(x))))
x=0.73453
print("Convert angle {0} from radians to degrees:".format(x,math.degrees(x)))
