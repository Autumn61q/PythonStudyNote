class Student:
    # 属性（成员变量）
    age=None #记得初始化为None啊
    
    # 行为（成员方法）（写在类内叫方法，写在类外叫函数）：
        # 语法：def 方法名(self,形参1,形参2,...):
                    # 方法体
                # self关键字是必须写的。它用来表示类对象自身。当我们
                # 使用类对象调用方法时，self会自动被python传入。在
                # 方法内部，想要访问类的成员变量，必须使用self
    def getAge(self):
        return self.age

xiaoming=Student() # 不要省略后面的括号，不然xiaoming的类型是type，加上之后才是__main__.Student
xiaoming.age=3
print(xiaoming.getAge())

