'''To shuffle randomly in place a list of elements'''
import random
n=int(input("Enter number of elments in list:"))
lst=[]
print("Enter elements in list:")
for i in range(0,n):
    lst.append(int(input()))
print("Original list=",lst)
random.shuffle(lst)
print("shuffled list=",lst)