n=int(input()) 
i=1     # i is to control the number of lines and the number of * in each line
large=(n+1)/2  #decide the maximum number of asterisks at the middle row
flag=True   # decide whether to execute condition 1 or condition 2
while i<=n:
    if i>0:
        j=1
        while j<=2*large+2*(i-1):  # use a while loop to guarantee enough * in each line
            if j%2==1:             # the character in each line which index is odd is Space
                print(" ",end='')
            else:
                if j<2*large-2*(i-1): # the character whose index is even but smaller than 2*n-2*(i-1) is space
                    print(" ",end='')
                else:                  # the character whose index is even and greater than or equal to 2*n-2*(i-1) is *
                    print("*",end='')
            j+=1
        print()
        if flag:             # conditon 1:the * in the next line is more than the last 
            i+=1
            if i==large+1:
                flag=False
                i-=2
        else:                # condition 2:the * in the next line is less than the last
            i-=1
    else:
        break  #end the program  
