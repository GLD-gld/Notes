#布尔表达式练习
True and True
False and True
1 == 1 and 2 == 1
"test" == "test"
1 == 1 or 2 != 1
True and 1 == 1
False and 0 != 0
True or 1 == 1
"test" == "testing"
1 != 0 and 2 == 1
"test" != "testing"
"test" == 1
not (True and False)
not (1 == 1 and 0 != 1)
not (10 == 1 or 1000 == 1000)
not (1 != 10 or 3 == 4)
not ("testing" == "testing" and "Zed" == "Cool Guy")
1 == 1 and not ("testing" == 1 or 1 == 0)
"chunky" == "bacon" and not (3 == 4 or 3 == 3)
3 == 3 and not ("testing" == "testing" or "Python" == "Fun")

#为什么"test" and "test"返回"test", 1 and 1 返回 1，而不是返回true呢？
# python和很多编程语言一样，都是给布尔表达式返回两个被操作对象中的一个，而非True或False。
# 这意味着，如果你写了False and 1， 得到的是第一个操作数（False），而True and 1，得到的是第二个操作数（1）。