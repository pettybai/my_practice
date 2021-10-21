#####################
# 装饰器

def singleton(cls):
    instance = {}

    def single(*args, **kwargs):
        if instance.get(cls) is None:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return single


class Singleton(object):
    def __init__(self, cls):
        Singleton.instance = {}
        self.cls = cls

    def __call__(self, *args, **kwargs):
        if Singleton.instance.get(self.cls) is None:
            Singleton.instance[self.cls] = self.cls(*args, **kwargs)
        return Singleton.instance[self.cls]


#####################
# __new__

class SingletonNew(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SingletonNew, cls).__new__(cls)
        return cls._instance


class student(SingletonNew):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)


a = student("king")
b = student("li")
c = student('liu')
a.get_name()
b.get_name()
