'''Compute percentage and class of student based on marks'''
marks= int(input("Enter total marks obtained: ")) 
per= (marks*100)/600 #Assuming total marks is 600 i.e. 100 for each of 6 subjects
if per<35:
    print("You have failed with a percentage of {:.2f}%.".format(per))
elif per>=35 and per<50:
    print("You have passed with a percentage of {:.2f}%.".format(per))
elif per>=50 and per<60:
    print("You have passed with a percentage of {:.2f}% and achieved third class.".format(per))
elif per>=60 and per<75:
    print("You have passed with a percentage of {:.2f}% and achieved second class.".format(per))
elif per>=75 and per<85:
    print("You have passed with a percentage of {:.2f}% and achieved first class.".format(per))
else:
    print("You have passed with a percentage of {:.2f}% and achieved distinction.".format(per))