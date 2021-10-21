# 文本文件的读写
# 二进制文件的读写，声音，视频等
with open('/mnt/c/Users/lilinjing/PycharmProjects/my_practice.py/file/miami.jpg', 'rb') as f:
    # image_data = f.readlines()    # image_data 是字节字符串格式的，而不是文本字符串
    for i in f:
        print(i)
# 对数据进行base64编码
import base64
with open('/mnt/c/Users/lilinjing/PycharmProjects/my_practice.py/file/miami.jpg', 'rb') as f:
    image_data = f.read()    # image_data 是字节字符串格式的，而不是文本字符串
    image_data_base = base64.b64encode(image_data)
    print(image_data_base)

# 写入二进制文件使用 'wb' 模式。