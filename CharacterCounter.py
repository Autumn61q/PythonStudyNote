"""
关于清除标点和特殊符号：
import string
user_input=input("请输入一个字符串：")
cleaned_input=user_input.translate(str.maketrans("","",string.punctuation))
"""
import string #记得这一步！
targetStr=list(input("Enter a string:").lower().translate(str.maketrans("","",string.punctuation)))
dict1=dict()
for ele in targetStr:
    dict1[ele]=targetStr.count(ele)
for ele in dict1:
    print(f"{ele}:{dict1[ele]}")
