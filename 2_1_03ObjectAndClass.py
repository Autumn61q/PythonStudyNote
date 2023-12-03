# 构造方法（就跟constructor一样）
    # 在创建类对象的时候，会自动执行
    # 在创建类对象的时候，将传入参数自动传递给__init__方法使用

class Student:

    # 谁懂，下面这三行甚至可以省略
    # name=None
    # age=None
    # tel=None

    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel

xiaoming=Student("xiaoming",19,12345)
print(xiaoming.age)
