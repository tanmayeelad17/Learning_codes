'''To generate random integer within a given range'''
import random
print("Enter the range")
strt=int(input("Enter start range:"))
end=int(input("Enter end range:"))
print("Random number:",random.randint(strt,end))