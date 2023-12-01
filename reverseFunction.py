!!!

def rev(user_input):
    preprocess=str(user_input)
    for i in range(int(len(preprocess)/2)):
        tem=preprocess[i]
        process=preprocess.replace(preprocess[i],preprocess[-1-i]).replace(preprocess[-1-i],tem)
    return process


print(rev(12345))