# 进程看成一个容器，则线程是此容器的工作单位
# 进程和线程的区别
# 进程之间是相互独立的，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，但互不影响；而同一个进程的多个线程是内存共享的，所有变量都由所有线程共享；
# 由于进程间是独立的，因此一个进程的崩溃不会影响到其他进程；
# 而线程是包含在进程之内的，线程的崩溃就会引发进程的崩溃，继而导致同一进程内的其他线程也奔溃

# GIL 锁的存在导致 Python 不能有效地使用多线程实现多核任务，因为在同一时间，只能有一个线程在运行


from threading import Thread, current_thread, Lock


def thread_test(name):
    print('thread %s  is running' % current_thread().name)
    print('hello', name)
    print('thread %s is over' % current_thread().name)



if __name__ == '__main__':
    print('thread %s is running' % current_thread().name)
    print('hello')
    t = Thread(target=thread_test, args=('test',), name='TestThread')
    t.start()
    t.join()
    print('thread %s ended' % current_thread().name)


num = 0

lock = Lock()


def cal():
    global num
    print('thread %s is running' % current_thread().name)
    for i in range(1000000):
        lock.acquire()
        num = num + 1
        lock.release()

    print('thread %s is end' % current_thread().name)


if __name__ == '__main__':
    print('%s' % current_thread().name)
    thread = []
    for i in range(5):
        thread.append(Thread(target=cal))
        thread[i].start()
    for i in range(5):
        thread[i].join()
    print('num %s' % num)
    print('%s' % current_thread().name)

# 