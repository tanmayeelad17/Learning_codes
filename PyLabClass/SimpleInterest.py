p = int(input("Enter principle amount: "))
t=int(input("Enter the time duration:"))
r=int(input("Enter the rate of interest:"))
SI=(p*t*r)/100
A1=p+SI
print("Simple interest in rs:",SI)
print("Total amount after adding simple interest:",A1)
CI=p*(((1+(r/100))**t)-1)
A2=p+CI
print("Compound interest in rs:",CI)
print("Total amount after adding compound interest:",A2)
