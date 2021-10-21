##############
# 函数三要素
# 函数名
# 函数参数
# 函数返回值
def my_func(x):
    return x * 3


print(my_func(6))


########################
# 函数的参数
# 必选参数
# 默认参数
# 可变参数
# 关键字参数

def my_func_must(x, y):
    return x + y


def my_func_default(x, y, z=9):
    return x + y + z


def my_func_tran(*args):
    s = 0
    for i in args:
        s = s + i
    return s


def my_func_dict(**kwargs):
    s = 0
    for i in kwargs.values():
        s = s + i
    return s


a = [87, 76, 56]
b = {'s': 78, 'c': 90, 'cd': 34}
print(type(**b))
print(my_func_tran(*a))
print(my_func_dict(**b))


#########################################
# 高阶函数
#
def func(fun, m=2, *x):
    return [fun(i, m) for i in x]


def muti(x, y):
    return x ** y


print(func(muti, 4, 4, 5, 6))

##########################################
# 内建高阶函数
# map，reduce，filer

a = [1, 20, 3, 9, 5, 6]
print(list(map(lambda x: x * x, a)))


def mult_2(x):
    return x * x


def mult_3(x):
    return x * x * x


def mult_4(x):
    return x * x * x * x


func_list = [mult_2, mult_3, mult_3]
print(list(map(lambda g: g(7), func_list)))

# reduce
from functools import reduce

print(reduce(lambda x, y: x if x > y else y, a))

print(reduce(lambda x, y: x * y, a))

# filter
print(list(filter(lambda x: x % 2, a)))


#########################################
# 匿名函数
# ：前是输入，：后是返回
# 临时的小巧函数


#########################################
# 闭包

