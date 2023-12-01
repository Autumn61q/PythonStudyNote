def find_repeated_number(user_input):
    for i in range(1,len(user_input)):
        if user_input[i] in user_input[:i]:
            return user_input[i]
        
print(find_repeated_number([2,4,1,6,4,1,2,4]))