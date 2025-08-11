'''Generate Pythagorean triplets upto a given max number'''
max=int(input("Enter a max value for generating Pythagorean triplets:")) 
for a in range(1,max-1):            # a should be less than max-1 because c should be greater than b
    for b in range(a+1,max):        # b should be greater than a and less than max because c should be greater than b
        for c in range(b+1,max+1):  # c should be greater than b and less than or equal to max
            if (a*a + b*b == c*c):  # Check if a, b, c form a Pythagorean triplet
                print(a,b,c)
            