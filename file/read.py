# io意味着input和output
# 读文件分为以下三个步骤
# 打开文件，读取文件，关闭文件
#
# try:
#     f = open('/mnt/c/Users/lilinjing/PycharmProjects/my_practice.py/file/text.txt', 'r')
#     data = f.read()
#     print(data)
# finally:
#     if f:
#         f.close()
#
# 一次性读取所有内容，使用 read() 或 readlines(),readlines将文件读成字符串列表
# 按字节读取，使用 read(size)；
# 按行读取，使用 readline()；

with open('/mnt/c/Users/lilinjing/PycharmProjects/my_practice.py/file/text.txt', 'r') as f:
    read_list = f.readlines()
    data = f.read()
    len(read_list)
    print(data)
    print((read_list))
    print(len(read_list))


def lazy_read(file_object, size):
    while True:
        piece = file_object.read(size)
        if not piece:
            break
        yield piece


with open('/mnt/c/Users/lilinjing/PycharmProjects/my_practice.py/file/text.txt', 'r') as f:
    for i in lazy_read(f, 10):
        print(i)

with open('/mnt/c/Users/lilinjing/PycharmProjects/my_practice.py/file/text.txt', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)

# 文件是可迭代对象
# 可以直接用for达到和内置读函数一样的效果
with open('/mnt/c/Users/lilinjing/PycharmProjects/my_practice.py/file/text.txt', 'r') as f:
    for i in f:
        print(i)

with open('/mnt/c/Users/lilinjing/PycharmProjects/my_practice.py/file/text.txt', 'r') as f:
    f_list = list(f)
    print(f_list)

# 写，追加——w,a
with open('/mnt/c/Users/lilinjing/PycharmProjects/my_practice.py/file/text.txt', 'a') as f:
    f.write('\nthree\n')
    f.write('four')
