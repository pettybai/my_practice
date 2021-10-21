# 一个函数返回了一个内部函数，该内部函数引用了外部函数的相关参数和变量，我们把该返回的内部函数称为闭包（Closure）


def make_pow(n):
    def inner(x):
        return pow(x, n)

    return inner


a = make_pow(2)
print(a(7))


##################################################
# 闭包的最大特点就是引用了自由变量，即使生成闭包的环境已经释放，闭包仍然存在。
# 闭包在运行时可以有多个实例，即使传入的参数相同。
# 闭包实现类
class point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def get_distance(self, u, v):
        return (self.x - u) ** 2 + (self.y - v) ** 2


# def point(x, y):
#     def get_distance(u, v):
#         return (x - u) ** 2 + (y - v) ** 2
#
#     return get_distance



init_point = point(4, 4)
print(init_point.get_distance(7, 8))
