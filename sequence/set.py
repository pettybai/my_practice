s = {'a', 'b', 'c', 'a', 'd', 'b'}
print(s)

str_set = set('lebron james')
print(str_set)

list_set = set([1, 1, 1, 13, 3, 3, 3, ])
print(list_set)

# 添加元素
list_set.add(9)
print(list_set)

# 删除元素
str_set.remove('a')
print(str_set)

# 集合运算
new_set = str_set | list_set
print(new_set)
print(new_set - list_set)
print(new_set & list_set)