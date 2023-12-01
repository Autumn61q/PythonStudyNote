def factorial(n):
    if n==0 :
        return 1
    i=1
    j=1
    while i<=n:
        j*=i
        i+=1
    return j
    
print(factorial(5))
