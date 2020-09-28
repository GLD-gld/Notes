#对象、类及从属关系
##Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


class Dog(Animal):

    def __init__(self, name):
        self.name = name
    
class Cat(Animal):

    def __init__(self, name):
        self.name = name

class Person(object):

    def __init__(self, name):
        self.name = name
        #确保类的self.pet属性被设置为默认None
        self.pet = None
    
class Employee(Person):

    def __init__(self, name, salary):
        #它会查找所有的超类，以及超类的超类，直到找到所需的特性为止。
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()