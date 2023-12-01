n=int(input())   
i=1
while i<=n:       # use i to control the number of lines
    j=1
    while j<=2*n+2*(i-1):  # the i line has 2*n+2*(i-1) characters
        if j%2==1:         # the character in each line which index is odd is Space
            print(" ",end='')
        else:
            if j<2*n-2*(i-1):     # the character whose index is even but smaller than 2*n-2*(i-1) is space
                print(" ",end='')
            else:                 # the character whose index is even and greater than or equal to 2*n-2*(i-1) is *
                print("*",end='')
        j+=1
    print()  # change to a new line
    i+=1