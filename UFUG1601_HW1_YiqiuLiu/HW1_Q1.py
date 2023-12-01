n=int(input())  
i=1   # i is to control the number of lines and the number of * in each line
if_flag=True # decide whether to execute condition 1 or condition 2
while i<=n:
    if i>0:
        j=1
        while j<=i:  # use a while loop to guarantee enough * in each line
            print("*",end='')
            j+=1
        print()    
        if if_flag:    # conditon 1:the * in the next line is more than the last 
            i+=1
            if i==n+1:
                if_flag=False
                i-=2
        else:          # condition 2:the * in the next line is less than the last
            i-=1
    else:
        break  #end the program        


