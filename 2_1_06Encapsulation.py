封装：
  1.私有成员变量：变量名以__(两个下划线开头）
  2.私有成员方法：方法名以__(两个下划线开头）
  
  class Test:
      __name=None
  
      def getName(self):
          return self.__name
      
      def __test():
          pass
  
  t1=Test()
  t1.__name="abab"# 不报错，但无效
  # t1.__test() # 报错
  print(t1.getName()) # 输出 None

继承：
  单继承语法：class 子类(父类名): 
                ...
  多继承语法：class 子类(父类名1，父类名2，...): 
                ...
              # 注：如果不同父类含有重名成员，如果不同的父
                    类含有重名成员，子类在继承时会按照"广
                    度优先"的顺序搜索属性。这意味着解释器
                    会先在子类中搜索属性，然后按照其在父类
                    元组中的顺序从左到右依次查找。
  覆写：就直接写就行
        class Base:
            def __init__(self):# 这里不要写成def __init__(self，name)
                self.name="xiaoming"
        
        class Derived(Base):
            def __init__(self):# 这里不要写成def __init__(self，name)
                self.name="daming"
        
        D1=Derived()
        print(D1.name)

  然后是乱七八糟的东西：
    class Base:
    info="Base"
    def __init__(self,info):
        print("Base construtor")
        self.name="xiaoming"
        self.info=info
        print(Base.info)

    class Derived(Base):
        info="Derived"
        def __init__(self):
            print("Derived constructor")
            self.name="daming"
    
    D1=Derived()
    B1=Base("这是传入的info")

    以上代码输出：Derived constructor
                 Base construtor
                 Base
    结论：Base.info和self.info不是一个东西
          子类对象实例化的时候不会调用父类的构造方法

    以及：https://blog.csdn.net/2201_75641637/article/details/129552892  后半部分很有意思

  关于如何访问父类的成员（乱七八糟结束）：
    1.访问父类方法
    class Parent:
      def parent_method(self):
          print("This is a method in Parent class")

    class Child(Parent):
        def child_method(self):
            Parent.parent_method(self)# 或者是改成super().parent_method()
            print(f"{self} is calling this method")
    
    c = Child()
    c.child_method()
    # 输出：
    # This is a method in Parent class
    # <__main__.Child object at 0x000002A5C936FD90> is calling this method
    2.访问父类属性（不太喜欢super，就只记了一种方法）
    class Base:
        info="这是父类默认的info"
        def __init__(self,info):
            print("Base construtor")
            self.info=info
            print(self.info)# print 这是子类传的info
        def getInfo(self):
            return self.info
    
    class Derived(Base):
        info="Derived"
        def __init__(self):
            Base.__init__(self,"这是子类传的info")
            print(Base.info)# print 这是父类默认的info
            print("Derived constructor")
            self.name="daming"
        def getBaseInfo(self):
            print(Base.getInfo(self))
        
    D1=Derived()
    D1.getBaseInfo()# print 这是子类传的info
