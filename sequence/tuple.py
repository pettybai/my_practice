num_tuple = (1, 2, 3, 4, 5, 6)

#################
# 一个元素的元组
tuple = (1,)
print(type(tuple))
tuple = (1)
print(type(tuple))

#########
# 通用操作索引，切片，迭代，相加，相乘
print(num_tuple[0])
print(num_tuple[4::-2])
print(6 in num_tuple)
print(num_tuple + num_tuple)
print(num_tuple * 3)
