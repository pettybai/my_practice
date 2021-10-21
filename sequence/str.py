test_str = "my girl is so lovely"
print(test_str)

#############
# 索引，切片，迭代，相加，相乘
print(test_str[5])
print(test_str[5::])
print("l" in test_str)
print(test_str, test_str)
print(test_str * 3)

###########
# 常用方法
# 字符串匹配，返回位置
print(test_str.find("girl"))

# 字符分割
print(test_str.split(" "))

# 字符拼接
list = test_str.split()
print(" ".join(list))

# 移除首尾的字符
test_str = test_str + "%%%"
print(test_str)
test_str = test_str.strip("%%%")
print(test_str)

# 替换对应字符
print(test_str.replace("so", "extremely"))

# 大小写转换
print(test_str.upper())

#