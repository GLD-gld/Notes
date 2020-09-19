#列表的操作
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]


while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool                 #以空格分割元素
print('#'.join(stuff[3:5])) # super stellar!        #以#分割元素

#列表
"""
    有序的列表
    要存储的东西
    随机访问
    线性
    通过索引
什么时候使用列表
    1.如果需要维持次序。指的是列表内容排序，列表不会自动为你按规则排序
    2.随机访问内容
    3.线性访问内容
"""