#自动化测试
以test_开头的测试函数，它们就是所谓的“测试用例”（test case），每一个测试用例里面都有一小段代码，
它们会创建一个或者一些房间，然后去确认房间的功能和你期望的是否一样。
这里最重要的函数是assert_equal,它保证了你设置的变量以及你在Room里设置的路径与你的期望相符。

export PYTHONPATH=.