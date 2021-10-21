#############
# 实例方法，类方法和静态方法


# 实例方法
class A(object):
    def foo(self):
        print('%s' % self)


# 类方法
class B(object):
    @classmethod
    def foo(cls):
        print('%s' % cls)


# 静态方法
class C(object):
    @staticmethod
    def foo():
        print(1)


a = A()
a.foo()
B.foo()
C.foo()
