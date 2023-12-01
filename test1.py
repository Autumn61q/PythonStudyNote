test=[2,4]

def bubblesort(test):
    for num in range(len(test)-1):
        for i in range(len(test)-1-num):
            if test[i]>test[i+1]:
                test[i],test[i+1]=test[i+1],test[i]
            i+=1
        num+=1
    print(test)

def quicksort(test,low,high):
    pivot=test[0]
    if len(test)==1:
        return
    i,j=low,high
    while i<j:
        while test[i]<=pivot and i<j:
            i+=1
        while test[j]>=pivot and i<j:
            j-=1
        if test[i]>test[j]:
            test[i],test[j]=test[j],test[i]
    pivot,test[i]=test[i],pivot
    quicksort(test,low,i-1)
    quicksort(test,j+1,high)

quicksort(test,0,len(test)-1)
print(test)
        


