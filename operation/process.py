# import os
#
# pid = os.fork()
#
# if pid < 0:
#     print('Fail to create process')
# if pid == 0:
#     print('I am child process (%s) and my parent is (%s).' % (os.getpid(), os.getppid()))
# if pid > 0:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# import os, time
# from multiprocessing import Process, Pool, Queue
#
#
# def child(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
#
# if __name__ == '__main__':
#     print('parent process is %s' % os.getpid())
#     p = Process(target=child, args=('test',))
#     print('child process will be start ')
#     p.start()
#     p.join()
#     p.close()
#     print('child process is over')
#     print('now cess is %s' % os.getpid())
# #
#
# def foo(x):
#     print('Run task is %x,pid is %s' % (x, os.getpid()))
#     time.sleep(2)
#     print('task %s,result %s' % (x, x * x))
#
#
# if __name__ == '__main__':
#     print('parent process is %s' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(foo, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')
#

def write_task(q):
    try:
        for i in range(5):
            print("write, %d" % i)
            q.put(i)
            time.sleep(1)
    except BaseException:
        print("write_task error")
    finally:
        print("write_task end")


def read_task(q):
    try:
        for i in range(5):
            print("read, %d" % q.get())
            time.sleep(1)
    except BaseException:
        print("read_task error")
    finally:
        print("read_task end")


if __name__ == "__main__":
    q = Queue()  # 父进程创建Queue，并传给各个子进程

    pw = Process(target=write_task, args=(q,))
    pr = Process(target=read_task, args=(q,))

    pw.start()  # 启动子进程 pw，写入
    pr.start()  # 启动子进程 pr，读取
    pw.join()  # 等待 pw 结束
    pr.join()  # 等待 pr 结束
    print('Done')
