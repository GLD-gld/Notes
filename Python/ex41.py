#学习面向对象术语
'''
类（class）：告诉Python创建新类型的东西。
对象（object）：两个意思，即最基本的东西，或者某样东西的实例。
实例（instance）：这是让Python创建一个类时得倒的东西。
def：这是在类里边定义函数的方法。
self：在类的函数中，self指代被访问的对象或者实例的一个变量。
继承（inheritance）：指一个类可以继承另一个类的特性，和父子关系类似。
组合（composition）：指一个类可以将别的类作为它的部件构建起来，有点儿像车子和车轮的关系。
属性（attribute）：类的一个属性，它来自于组合，而且通常是一个变量。
是什么（is-a）：用来描述继承关系，如Salmon is-a Fish（鲑鱼是一种鱼）。
有什么（has-a）：用来描述某个东西是由另外一些东西组成的，或者某个东西有某个特征，如Salmon has-a mouth（鲑鱼有一张嘴）。
'''

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and @@@params.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

#do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

#load uo the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding='utf-8'))

print(f"WORDS==={WORDS}")

def convert(snippet, phrase):
    #capitalize()函数将字符串的第一个字母变成大写,其他字母变小写。对于 8 位字节编码需要根据本地环境。
    #random.sample()函数在 多个字符中选取指定数量的字符组成新字符串
    #count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
    class_names = [w.capitalize() for w in 
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    # print(snippet.count("%%%"))
    # print(random.sample(WORDS,snippet.count("%%%")))
    # print(snippet.count("***"))
    # print(random.sample(WORDS,snippet.count("***")))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        print(f"i==={i}")
        #randint()随机整数
        param_count = random.randint(1,3)
        print(f"param_count==={param_count}")
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))
        print(f"param_names==={param_names}")
    
    for sentence in snippet, phrase:
        print(f"sentence==={sentence}")
        #复制列表的方法。使用“列表切片”（list slicing）语法[:]对列表中的所有元素进行切片操作。
        result = sentence[:]

        #fake class names
        for word in class_names:
            #replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
            result = result.replace("%%%", word, 1)

        #fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        #fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
        
        results.append(result)
    print(f"results{results}")
    return results

#keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        # print(f"snippets==={snippets}")
        random.shuffle(snippets)

        for snippet in snippets:
            print(f"snippet==={snippet}")
            phrase = PHRASES[snippet]
            print(f"phrase==={phrase}")
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

                print(question)

                input("> ")
                print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")