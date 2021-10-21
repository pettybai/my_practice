# 生成器的方法非常简洁，不用自定义 __iter__() 和 next() 方法
# 简而言之，就是 next 使函数执行，yield 使函数暂停

def Fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a, b


fib = Fib()
for i in range(10):
    print(fib.__next__())

# send() throw() close()

