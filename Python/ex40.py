#模块、类和对象
# 模块：
#     1.模块是包含函数和变量的Python文件。
#     2.可以导入这个文件。
#     3.然后可以使用.操作符访问模块中的函数和变量

# 类：
#     1.可以通过一组函数和函数放到一个容器中，从而用"."运算符访问它们。
#     2.需实例化
#     例：
# class MyStuff(object):

#     def __init__(self):
#         self.tangerine = "And now a thousand years between"    
    
#     def apple(self):
#         print("I AM CLASSY APPLES!")

# thing = MyStuff()
# thing.apple()
# print(thing.tangerine)
# 1.Python 查找MyStuff()并且知道了它是你定义过的一个类。
# 2.Python创建了一个空对象，里边包含了你在该类中用def指定的所有函数。
# 3.然后Python回去检查你是不是在里边创建了一个__init__“魔法”函数，如果有创建，它就会调用这个函数，从而对你新创建的空对象实现了初始化。
# 4.在MyStuff的__init__函数里，有一个多余的函数叫self，这就是Python为你创建的空对象，而你可以对它进行类似模块、字典等的操作，为它设置一些变量。
# 5.在这里，把self.tangerine设成了一段歌词，这样我就初始化了该对象。
# 6.最后Python将这个新建的对象赋给一个叫thing的变量，以供后面使用。

# 1.类就像一种蓝图或者一种预定义的东西，通过它可以创建新的迷你模块。
# 2.实例化的过程相当于你创建类这么一个迷你模块，而且同时导入了它。“实例化”的意思就是从类创建一个对象。
# 3.结果创建的迷你模块就是一个对象，你可以将它赋给一个变量供后续操作。


class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
        
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


#为什么创建__init__或者别的类函数时需要多加一个self变量？
# 如果不加self，cheese = 'Frank'这样的代码就有歧义了，它指的既可能是实例的cheese属性，也可能是一个叫cheese的局部变量。
# 有了self.cheese = 'Frank'就清楚地知道着指的是实例的属性self.cheese。