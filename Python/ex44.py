#继承和组合
#什么是继承？
#继承就是用来指明一个类的大部分功能或全部功能都是从一个父类中获得的。
# class Foo(Bar) : 创建一个叫Foo的类，并让它继承自Bar。

#父类和子类有3种交互方式
# 1.子类上的动作完全等同于父类上的动作。
# 2.子类上的动作完全覆盖类父类上的动作。
# 3.子类上的动作部分替换了父类上的动作。

# 隐式继承
#父类里定义类一个函数但没有在子类中定义时会发生隐式行为。
class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

#显示覆盖
class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()

#在运行前或运行后替换
class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    
    def altered(self):
        print("CHILD, BEFORE altered()")
        #用Child和self这两个参数调用super，然后在此返回的基础上调用altered。
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()

#要用super()的原因：为解决多重继承
# class SuperFun(child, BadStuff):
#     pass
#这相当于创建了一个叫SuperFun的类，同时继承了两个类。一旦在SuperFun实例上调用任何隐式动作，Python就必须回到Child和BadStuff的
#类层次结构中查找可能的函数，而且必须要用固定的顺序去查找。因此Python使用了一个叫“方法解析顺序”（method resolution order，MRO）
#的东西，还用了一个叫C3的算法。Python提供super()函数来处理这一切。

#super()和__init__搭配使用
#super()函数最常见的用法是在基类的__init__函数中使用。通常也是唯一可以进行这种操作的地方。
#在这里你需要在子类里做了一些事情，然后在父类中完成初始化。例：
class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()
#在__init__里边先设了一些变量，然后才让Parent用Parent.__init__完成初始化。

#组合
class Other(object):

    def override(self):
        print("OTHER override()")
    
    def implicit(self):
        print("OTHER implicit()")
    
    def altered(self):
        print("OTHER altered()")
    
class Child(object):
    
    def __init__(self):
        #变量是一个对象
        self.other = Other()
    
    def implicit(self):
        #定义一个函数来完成它的功能
        self.other.implicit()

    def override(self):
        print("CHILD override()")
    
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()