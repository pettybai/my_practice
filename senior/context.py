# 什么是上下文？其实我们可以简单地把它理解成环境
# 进程上下文指的是一个进程在执行的时候，CPU 的所有寄存器中的值、进程的状态以及堆栈上的内容等，当系统需要切换到其他进程时，系统会保留当前进程的上下文，也就是运行时的环境，以便再次执行该进程。
# 上下文管理器协议，是指要实现对象的 __enter__() 和 __exit__() 方法

from math import sqrt, pow


class Point(object):
    def __init__(self, x, y):
        print('init')
        self.x, self.y = x, y

    def __enter__(self):
        print('enter context')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit context')

    def print_test(self):
        print('test')

    def get_distance(self):
        return sqrt(self.x ** 2 + self.y ** 2)


# with 会调用__init__上下文管理器
# 调用___enter__()方法,并把返回值as后的变量pt
# 执行语句体
# 不管执行过程中是否发生异常，都执行上下文管理器的 __exit__() 方法。
# __exit__() 方法负责执行『清理』工作，如释放资源，关闭文件等
with Point(3, 4) as pt:
    print('distance: ', pt.get_distance())

# 内建对象
# 文件打开，with 等价 try finally
import os

print(os.getcwd())

file = open('Iterator.py', 'r')
try:
    for line in file:
        print(line)
finally:
    file.close()

with open('Iterator.py', 'r') as file:
    for line in file:
        print(line)

# from contextlib import contextmanager
#
#
# @contextmanager
# def fib():
#     a, b = 0, 1
#     while True:
#         yield a, b
#         a, b = b, a + b
#
#
# with fib() as f:
#     for i in range(29):
#         print(f)

