def reverse(user_input):
    pro=str(user_input)
    res=""
    for i in range(len(pro)-1,-1,-1):
        res+=pro[i]
        i+=1
    return res

print(int(reverse(12345)))
