#Student details using list and tuple

n=int(input("Enter number of students:"))
input_tuple=()
students=[]
flag=False
print("Enter the details of each student")
for i in range(0,n):
    name=input("Name:")
    age=int(input("Age:"))
    avg=float(input("Average marks:"))
    input_tuple=(name,age,avg)
    students.append(input_tuple)
S=input("Enter the name of student whose details u want to know:")
for x in students:
    if x[0]==S:
        flag=True
        print("Name=",x[0],"Age=",x[1],"Average marks=",x[2])
if flag==False:
    print("No student found!")