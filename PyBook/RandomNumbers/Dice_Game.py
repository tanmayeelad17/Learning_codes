import random
print("User 1 is computer")
print("User 2 is Human")
print("The highest value on dice decides winner")
ans='y'
while ans=='y':
    diceUser1=random.randrange(1,7)
    print("Computer plays:",diceUser1)
    diceUser2=random.randrange(1,7)
    print("human plays:",diceUser2)
    if diceUser2>diceUser1:
        print("Human winner!")
    elif diceUser1==diceUser2:
        print("Tie!")
    else:
        print("Computer Winner!")
    ans=input("Do u want to play angain? y or n:")