# list,tuple,string,dict,set
num_list = [1, 2, 3, 4, 5, 6]
tuple = (1, 2, 3, 4, 5, 6)
string = '123456'
dict = {"a": 1, "b": 2, "c": 3}

#####################
# 通用操作，索引，分片，迭代，加，乘
for i in range(1,5):
    print(i)

# 索引
print(num_list[1])

# 左索引:右索引:步长
print(num_list[1:5:2])
print(num_list[5:0:-2])

# 同序列加
print(num_list + list(tuple))

# 乘
print(num_list * 2)

# 元素是否在序列
print(5 in num_list)

##################
# 常用list的方法
# list是可变的，str和元组是不可变的
# 需要做转换
print(list(string))
print(list(tuple))

# 由元素找到索引
print(num_list.index(6))

# 统计元素出现的次数
print(num_list.count(5))

# 添加新元素
num_list.append(8)
print(num_list)

# 合并列表
num_list.extend(list(tuple))
print(num_list)

# 将某个元素添加到某个位置
num_list.insert(3, 9)
print(num_list)

# 删除末尾元素
print(num_list.pop())

# 删除匹配元素
num_list.remove(9)
print(num_list)

# 列表元素反转
num_list.reverse()
print(num_list)

# 列表排序
# sorted返回新列表，sort改变原来的列表
print(sorted(num_list, reverse=False))
num_list_1 = num_list.copy()
num_list.pop()
print(num_list_1)
print(num_list)
for i in range(5):
    print(i)
