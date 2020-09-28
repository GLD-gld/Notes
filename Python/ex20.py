#函数和文件
from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    # print(f.tell())
    f.seek(0) #seek()函数用于将文件指针移动至指定位置
    # print(f.tell())

def print_a_line(line_count, f):
    print(line_count, f.readline(), end="") #end="" : 打印时不会添加一个\n

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)


#文件指针的移动
#tell()函数用于判断文件指针当前所处的位置。
    #语法格式:file.tell()
#seek()函数用于移动文件指针到文件的指定位置。
    #语法格式:file.seek(offset[, whence])
    #file：表示文件对象；
    #whence：作为可选参数，用于指定文件指针要放置的位置，该参数的参数值有 3 个选择：0 代表文件头（默认值）、1 代表当前位置、2 代表文件尾。
    #offset：表示相对于 whence 位置文件指针的偏移量，正数表示向后偏移，负数表示向前偏移。

#例：
# 当whence == 0 &&offset == 3（即 seek(3,0) ），表示文件指针移动至距离文件开头处 3 个字符的位置；
# 当whence == 1 &&offset == 5（即 seek(5,1) ），表示文件指针向后移动，移动至距离当前位置 5 个字符处。

#readline()函数返回的内容中包含文件本来就有的\n，而print在打印时又会添加一个\n，这样就会多出一个空行。
#print时多加一个参数end=""可以解决。
