# 很简单的构想
# 同一线程会进行内存共享
# 意味着对变量做修改会影响其他线程
# 那怎么将线程和变量绑定呢？局部变量，全局字典绑定，ThreadLocal

# 局部变量
from threading import Thread, current_thread, local

# def echo(num):
#     print(current_thread().name, num)
#
#
# def calc():
#     print(current_thread().name + 'is running')
#     local_num = 0
#     for i in range(10000):
#         local_num = local_num + 1
#     echo(local_num)
#     print(current_thread().name + 'is end')
#
#
# if __name__ == '__main__':
#     print(current_thread().name + 'is running')
#     threads = []
#     for i in range(5):
#         threads.append(Thread(target=calc))
#         threads[i].start()
#     for i in range(5):
#         threads[i].join()
#     print(current_thread().name + 'is end')
#

# 全局字典
# global_dict = {}
#
#
# def echo():
#     num = global_dict[current_thread()]
#     print(current_thread().name, num)
#
#
# def cal():
#     print(current_thread().name + ' is running')
#     global_dict[current_thread()] = 0
#     for i in range(10000):
#         global_dict[current_thread()] = global_dict[current_thread()] + 1
#     echo()
#     print(current_thread().name + ' is end')
#
#
# if __name__ == '__main__':
#     print(current_thread().name + ' is running')
#     thread = []
#     for i in range(5):
#         thread.append(Thread(target=cal))
#         thread[i].start()
#     for i in range(5):
#         thread[i].join()
#     print(current_thread().name + 'is end')
#
# threadLocal
globel_data = local()


def echo():
    print(current_thread().name, globel_data.num)


def cal():
    print(current_thread().name + ' is running')
    globel_data.num = 0
    for i in range(10000):
        globel_data.num = globel_data.num + 1
    echo()
    print(current_thread().name + ' is end')


if __name__ == '__main__':
    print(current_thread().name + ' is running')
    thread = []
    for i in range(5):
        thread.append(Thread(target=cal))
        thread[i].start()
    for i in range(5):
        thread[i].join()
    print(current_thread().name + 'is end')
