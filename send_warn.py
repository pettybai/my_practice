import requests


def send_mobile_warn():
    playload = {'name': 'gdxx02', 'pwd': 'gdxxzx53550', 'dst': '17862959331,15663427953',
                'msg': 'I love you'.encode('gbk')}
    try:
        requests.get(url='http://yl.mobsms.net/send/gsend.aspx', params=playload)
    except Exception as e:
        print("send_mobile_error:{}\n".format(e))


if __name__ == '__main__':
    send_mobile_warn()
