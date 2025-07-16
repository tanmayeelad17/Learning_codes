q=int(input("Enter the quantity of items:"))
p=float(input("Enter the price per item:"))
tc=q*p
print("Total cost of the products is: Rs ",tc)
Fc="Rs {:.2f}".format(tc)
print("Total cost upto 2 decimal is: Rs",Fc)
