def is_prime(a):
    for num in range(2,a):
        if a%num==0:
            return False
        else:
            return True
    return False
        
result=is_prime(7)
print(result)