# 继承和多态


class Animal(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        print('%s' % self.name)


class Dog(Animal):
    def greet(self):
        print('wangwang,%s' % self.name)

    def run(self):
        print('%s,I am running' % self.name)


class Cat(Animal):
    def greet(self):
        print('miaomiao,%s' % self.name)


animal = Animal('dog')
dog = Dog('dog')
cat = Cat('cat')
animal.greet()
dog.greet()
cat.greet()
dog.run()

