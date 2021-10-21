# 子程序是协程的特例
# 一个子程序就是一次函数调用，它只有一个入口，一次返回
# 协程允许有多个入口对程序进行中断、继续执行等操作
# yield 实现简单的生产-消费者模型


import time


def consumer():
    message = ''
    while True:
        n = yield message
        if not n:
            return
        print('[consumer] consuming %s .....' % n)
        time.sleep(2)
        message = '200 OK'


def produce(c):
    c.__next__()
    i = 0
    _sum = []
    while i < 100:
        _sum.append(i)
        i = i + 1
        print('[producer] producing %s....' % _sum)
        r = c.send(i)
        print('[producer] consumer return %s....' % r)
    c.close()


if __name__ == '__main__':
    c = consumer()
    produce(c)

# import time
#
# def consumer():
#     message = ''
#     while True:
#         n = yield message     # yield 使函数中断
#         if not n:
#             return
#         print ('[CONSUMER] Consuming %s...' % n)
#         time.sleep(2)
#         message = '200 OK'
#
# def produce(c):
#     c.__next__()         # 启动生成器
#     n = 0
#     while n < 5:
#         n = n + 1
#         print ('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)  # 通过 send 切换到 consumer 执行
#         print ('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
# if __name__ == '__main__':
#     c = consumer()
#     produce(c)
