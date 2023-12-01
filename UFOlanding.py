user_input = [2, 3, 4, 3, 2, 5]
def determine(user_input):
    for i in range(1,len(user_input)):
        for j in range(i-1,0-1,-1):
            if user_input[i]==user_input[j]:
                return user_input[i]
            
print(determine(user_input))