# __new__
# __str__ , __repr__
# __iter__
# __getitem__ , __setitem__ , __delitem__
# __getattr__ , __setattr__ , __delattr__
# __call__

# __new__创建实例，在__init__之前调用


class A(object):
    set_flag = dict()

    def __new__(cls):
        if cls.set_flag.get('example'):
            cls.set_flag['example'] = cls.set_flag['example'] + 1
            print('exist')
            print(cls.set_flag['example'])
        else:
            print('new')
            print('no')
            cls.set_flag['example'] = 1

    def __init__(self):
        print('__init__')


a = A()
b = A()


# __str__ __repr__
class B(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class C(B):
    def __str__(self):
        return self.name

    __repr__ = __str__


d = B('dog')
e = C('cat')
print(d)
print(str(d))
print(e)


# __iter__可迭代对象

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a, self.b


fib = Fib()
for i in fib:
    if i[1] > 100:
        break
    print(i)


# __getitem__

class Fib_Slice(Fib):
    def __getitem__(self, item):
        _fib_list = list()
        if isinstance(item, slice):
            self.begin, self.end = item.start, item.stop
            i = 0
            for j in self:
                i = i + 1
                if i == self.end:
                    break
                if i > self.begin or i == self.begin:
                    _fib_list.append(j)

            return _fib_list
        if isinstance(item, int):
            i = 0
            for j in self:
                i = i + 1
                if i == item:
                    return j


fib_slice = Fib_Slice()
print(fib_slice[1:9])


# __setitem__ __delitem__

class Point(object):
    def __init__(self):
        self.ding = {}

    def __setitem__(self, key, value):
        self.ding[key] = value

    def __delitem__(self, key):
        self.ding.pop(key)

    def __getitem__(self, item):
        return self.ding.get(item)


point = Point()
point['x'] = 1
point['y'] = 2
print(point['x'])


# __getattr__ __delattr__ __setattr

# __call__

class Point_Call(Point):
    def __call__(self, *args, **kwargs):
        s = 0
        for i in self.ding.values():
            s = s + i * i
        return s


point = Point_Call()
point['x'] = 10
point['y'] = 20
print(point())

# __slot__限定允许绑定的属性

point['z'] = 30

print(point['z'])


class Point_Call_Slot(Point_Call):
    __slots__ = {'ding'}


point = Point_Call_Slot()

point['z'] = 30
print(point.z)


