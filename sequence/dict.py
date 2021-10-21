test_dict = {"li": "深信服", "lin": "shopee", "jing": "world"}

##########################
# 创建字典
test_dict_1 = {}

# 更新字典
test_dict_1['guo'] = '郭郭'
print(test_dict_1)

test_dict_2 = dict(guo='郭郭')
print(test_dict_2)

item = [('guo', '郭郭')]
print(dict(item))

# 遍历字典
for i in test_dict.keys():
    print(i)
print('li' in test_dict)

######################
# 清空字典
test_dict_3 = test_dict_1
print(test_dict_3)
test_dict_3 = {}
print(test_dict_1)

test_dict_1 = test_dict_3
test_dict_3.clear()
print(test_dict_1)

# 复制
# 可变对象同步，不可变对象修改
test_dict['book'] = ['sky', 'law']
test_dict_copy = test_dict.copy()
test_dict_copy['book'].pop()
print(test_dict)

test_dict_copy['li'] = 'God'
print(test_dict)

# 避免keyerror
print(test_dict.get('li'))

# 设定默认值
# 没有则更新
test_dict.setdefault('li', 'test')
test_dict.setdefault('God', 'li')
print(test_dict)

# 合并字典
test_dict.update(test_dict_2)
print(test_dict_2)
print(test_dict)
print(test_dict)

# 遍历
print(list(test_dict.items())[0])
print(test_dict.keys)
for i in test_dict.keys():
    print(i)

for i in test_dict.values():
    print(i)

for i, j in test_dict.items():
    print(i)

# 删除某个键值对
test_dict.pop('guo')
print(test_dict)

# 排序

students = [
    {'name': 'john', 'score': 'B', 'age': 15},
    {'name': 'jane', 'score': 'A', 'age': 12},
    {'name': 'dave', 'score': 'B', 'age': 10},
    {'name': 'ethan', 'score': 'C', 'age': 20},
    {'name': 'peter', 'score': 'B', 'age': 20},
    {'name': 'mike', 'score': 'C', 'age': 16}
]

print(sorted(students, key=lambda stu: stu['age']))
