'''To demonstrate choice function for random selection from a sequence'''
import random
lst=['d','f','s','p']
ch=random.choice(lst)
print("Random choice is:",ch)
if ch=='d':
    print("Distiction")
if ch=='f':
    print("First class")
if ch=='s':
    print("Second class")
if ch=='p':
    print("Pass")