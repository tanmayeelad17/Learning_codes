'''Program to check a given number is palindrome or not'''
num=int(input("Enter a integer number:"))
rev=0 # Initialize reverse number
temp=num # Temporary variable to hold the original number
while temp>0:                # Loop until temp becomes 0
    rev=(10*rev) + (temp%10) # Get the last digit and add it to rev
    temp=temp//10            # Remove the last digit from temp
if num==rev:                # Check if original number is equal to reversed number
    print("{} is a Palindrome".format(num)) # If equal, it's a palindrome
else:
    print("{} is Not a Palindrome".format(num))