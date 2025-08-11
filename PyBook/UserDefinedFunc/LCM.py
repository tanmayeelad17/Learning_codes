'''Program using user defined function to find LCM of two numbers'''

def GCD(a,b):
    if a<b:
         t=a
         a=b
         b=t
    
    rem=a%b
    while rem!=0:
        a=b
        b=rem
        rem=a%b
    return b 

def Lcm(a,b):
    l_c_m=(a*b)//GCD(a,b)      
    return l_c_m

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
Lcm(a,b)
print("LCM of", a, "and", b, "is", Lcm(a,b))