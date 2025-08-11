'''To compute a number is prime or not'''
num=int(input("Enter number:"))
prime=True
divisor=2
while divisor<=(num/2):
    if num%divisor == 0:
        prime=False
        print("{} is Not prime".format(num))
        break
    divisor+=1
if prime:
    print("{} is Prime".format(num))