#用户输入进阶
#词汇元组（tuple）
# 元组其实就是一个不能修改的列表。
# 创建方法和创建列表差不多，成员之间需要用逗号隔开，然后放到圆括号中。
# first_word = ('verb', 'go')
# second_word = ('direction', 'north')
# third_word = ('direction', 'west')
# sentence = [first_word, second_word, third_word]
#这样就创建了一个（TYPE，WORD）组，让你识别出单词，并且对它执行指令。


#扫描输入

# #异常和数值
# def convert_number(s):
#     try:
#         return int(s)
#     except ValueError:
#         return None


lexicon = {
    "north": 'direction',
    "south": 'direction',
    "east": 'direction',
    "west": 'direction',
    "go": 'verb',
    "kill": 'verb',
    "eat": 'verb',
    "the": 'stop',
    "in": 'stop',
    "of": 'stop',
    "bear": 'noun',
    "princess": 'noun',
    "1234": 'number',
    "3": 'number',
    "91234": 'number',
    "IAS": 'error',
    "ASDFADFASDF": 'error'
}

def scan(sentence):
    results = []
    words = sentence.split()
    for word in words:
        word_type = lexicon.get(word)
        try:
            results.append((word_type, int(word)))
        except ValueError:
            results.append((word_type, word))
    return results