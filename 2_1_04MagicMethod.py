2_1_04 的__init__构造方法，就是Python类的内置方法之一
这些内置的类方法，各有各的特殊功能，称之为魔术方法（特征就是名称前后各有两个下划线）。
这里介绍几个常见的


1.__str__

  class Student:
      pass  # 写了一个抽象的接口相当于是
  
  xiaoming=Student()
  print(xiaoming) 
# 上面那个代码会输出这个对象的内存地址。但是要地址基本就是没用，所
#  以说我们可以用 __str__ 来控制类转化成字符串的行为

可以改成这样
  class Student:
      def __str__(self):
          return "好好学习"
  
  xiaoming=Student()
  print(xiaoming) # 输出  好好学习
  print(type(xiaoming)) # 输出  <class '__main__.Student'>



2.__lt__ （less than）（小于符号比较方法）（跟重载运算符一样）

  class Student:
      def __init__(self,age):
          self.age=age
  
      def __lt__(self,other):# other是自己取的
          return self.age<other.age
  
  xiaoming=Student(3)
  daming=Student(5)
  print(xiaoming<daming)

3.__le__ （less than or equal to）

  class Student:
      def __init__(self,age):
          self.age=age
  
      def __le__(self,other):# other是自己取的
          return self.age<=other.age
  
  xiaoming=Student(3)
  daming=Student(3)
  print(xiaoming<=daming)
我想说的是，你可能觉得lt里面的函数实现改一改就能变成le，是的。但
是其实函数的实现不重要，更重要的是xiaoming<=daming是不是valid。

4.__eq__ (equal to)
