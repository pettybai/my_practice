# 迭代和可迭代对象
# 含有 __iter__() 方法或 __getitem__() 方法的对象称之为可迭代对象。
from collections import Iterable

print(hasattr([1, 2, 3], '__iter__'))
print(isinstance([1, 3, 4], Iterable))

# 迭代器（Iterator）指遵循迭代器协议（iterator protocol）的对象,是指要实现对象的 __iter()__ 和 next() 方法

from collections import Iterator

print(hasattr([1, 2, 3], 'next'))
print(isinstance([1, 2, 3], Iterator))
print(isinstance(iter([1, 2, 3]), Iterator))


# Iterator

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a, self.b


def main():
    fib = Fib()
    for i in range(10):
        print(fib.__next__())
if __name__== '__main__':
    main()