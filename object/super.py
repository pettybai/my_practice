# 你不知道的super
# 如何应用


class Animal(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print('Hello, I am %s.' % self.name)


class Dog(Animal):
    def greet(self):
        super(Dog, self).greet()
        print('wangwang')


dog = Dog('dog')
dog.greet()


# 深入super
# MRO解析顺序

class Base(object):
    def __init__(self):
        print('enter base')
        print('leave base')


class A(Base):
    def __init__(self):
        print('enter a')
        super(A, self).__init__()
        print('leave a')


class B(Base):
    def __init__(self):
        print('enter b')
        super(B, self).__init__()
        print('leave b')


class C(A, B):
    def __init__(self):
        print('enter c')
        super(C, self).__init__()
        print('leave c')

        print('enter c')
        super(B, self).__init__()
        print('leave c')


_test = C()
_test
