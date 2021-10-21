#################
# 对象可以看做是由数据（或者说特性）以及一系列可以存取、操作这些数据的方法所组成的集合
# 继承，多态 ，封装


# 类和实例


class Animal(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("I am a %s" % self.name)


dog = Animal('wangwang')
print(dog.name)
dog.greet()


#######################
# 访问限制

class Animal_New(object):
    def __init__(self, name, heart):
        self.name = name
        self.__heart = heart


cat = Animal_New('miaomiao', "nice")
print(cat.name)
# print(cat.__heart)

#####################
# 获取对象信息

# type
print(type(dog))

# isinstance
print(isinstance(dog, Animal))

# attr
print(hasattr(dog, 'name'))
print(hasattr(dog, 'age'))

print(getattr(dog, 'name'))
# print(getattr(dog, 'age'))

setattr(dog, 'age', 12)
print(dog.age)

# dir
print(dir(dog))
