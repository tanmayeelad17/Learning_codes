#find positive and negative numbers in a given list
list1=[-1,-2,-3,-4,1,2,3,4,5,0]
x=len(list1)
plist=[]
nlist=[]

for i in range(x):
    if list1[i]>0:
        plist.append(list1[i])
    if list1[i]<0:
        nlist.append(list1[i])
print("list of positive numbers=",plist)
print("List of negative numbers=",nlist)