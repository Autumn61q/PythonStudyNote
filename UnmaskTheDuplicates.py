user_input = [4, 60, 4, 70, 60, 72]
result=set()
for i in range(len(user_input)):
    if user_input.count(user_input[i])!=1:
        result.add(user_input[i])
print(list(result))