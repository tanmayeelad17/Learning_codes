'''Using functions generate Floyd's triangle for a given number of rows'''
def Floyd(n):
    a=1              # Initialize the first number to print
    for i in range(1,n+1):      # Loop through each row
        for j in range(0,i):    # Loop through each column in the row
            print(a," ",end='')
            a+=1
        print()  # Move to the next line after each row
    print()  # Print a newline at the end
n=int(input("Enter the number of rows for Floyd's triangle: "))
Floyd(n)