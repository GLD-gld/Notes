#参数、解包和变量
from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("This script is called:", script)
print("Your second variable is:", second)
print("Your third variable is:", third)