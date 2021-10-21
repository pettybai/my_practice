
def cal(_str):
    dig = ""
    _res = 0
    for i in _str:
        if i.isdigit():
            dig = dig + i
        elif i == "T":
            _res = _res + int(dig) * 1024 * 1024
            dig = ""
        elif i == "G":
            _res = _res  + int(dig) * 1024
            dig = ""
        elif i == "M":
            _res = _res  + int(dig)
    return _res
save_list = ["1024G","2M","1T"]

save_dict = {}
for i in save_list:
    save_dict[i] = cal(i)
_dict = sorted(save_dict.items(),key = lambda x: x[1])
for i in _dict:
    print(i[0])
