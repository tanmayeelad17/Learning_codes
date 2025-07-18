'''Generate a unique list of values from a given population of values'''
import random
population=list(input("Enter values in list:"))
print("Population of sequence=",population)
x=int(input("Enter number of elements in unique list:"))
z=random.sample(population,x)
print("Random unique list=",z)