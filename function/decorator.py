###########################
# 装饰器就是一个返回函数的高阶函数，一种高阶函数的用法
# 装饰器其实就是一个语法糖，存在参数传值的顺序
#


def print_func_name_first(func):
    def wrap():
        print(func.__name__)
        return func

    return wrap


def runtime():
    import time
    start = time.time()

    def decorator(func):
        def wrap(*args, **kwargs):
            return func(*args, **kwargs)

        return wrap

    end = time.time()
    print(end - start)
    return decorator


def print_func_name_second(func):
    def print_func(x, y):
        print(func.__name__)
        return func(x, y)

    return print_func


def print_func_name_thrid(func, add_str):
    def wrap(*args):
        print(add_str + func.__name__)
        return func(args[0], args[1])

    return wrap


def print_func_name_laste(add_str):
    def decorator(func):
        def wrap(*args):
            print(add_str + func.__name__)
            return func(args[0], args[1])

        return wrap

    return decorator


def hello_():
    print('hello')


def add(x, y):
    print(x + y)


# print_func_name_first(hello_)()
# print_func_name_second(add)(2, 3)
# print_func_name_thrid(add, 'the_function_name:')(3, 4)


@print_func_name_laste('skr skr: ')
def add(x, y):
    print(x + y)


@runtime()
def run_add(*args):
    s = 1
    for i in args:
        s = s * i
    print(s)


# add(7, 9)
run_add(1, 2)
