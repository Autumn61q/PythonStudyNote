class Student:
    age=None #记得初始化为None啊

xiaoming=Student() # 不要省略后面的括号，不然xiaoming的类型是type，加上之后才是__main__.Student
xiaoming.age=3
print(xiaoming.age)
