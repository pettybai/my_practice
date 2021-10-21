import smtplib, requests, datetime
from email.mime.text import MIMEText
from email.header import Header


def send_mail_warn():
    """
    发送预警
    :return:
    """
    mail_info = {
        'mail_host': "smtp.qq.com",
        'mail_port': 465,
        'mail_user': '2386030719@qq.com',
        'mail_pass': 'atepmbwxbznadiia',
        'mail_sender': '2386030719@qq.com',
        'mail_receivers': ['2386030719@qq.com', 'lilinjing@inspur.com', 'dfjgkdjfgvfljv@qq.com']
    }

    message = MIMEText('人力系统无法访问...', 'plain', 'utf-8')
    message['Subject'] = Header("告警信息", 'utf-8')
    message['From'] = Header("Inspur", 'utf-8')  # 发送者
    message['To'] = Header("测试", 'utf-8')  # 接收者
    message['Date'] = Header(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), 'utf-8')

    try:
        # ready
        smtpObj = smtplib.SMTP_SSL(mail_info['mail_host'], mail_info['mail_port'])
        # smtpObj = smtplib.SMTP(mail_info['mail_host'], 465)
        smtpObj.login(mail_info['mail_user'], mail_info['mail_pass'])
        for i in mail_info['mail_receivers']:
            # send
            smtpObj.sendmail(
                mail_info['mail_sender'], i, message.as_string())
        # quit
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('sen_mail_error', e)


def send_mobile_warn():
    playload = {'name': 'gdxx02', 'pwd': 'gdxxzx53550', 'dst': '15663427953,17853142392', 'msg': '你是聪明的汪汪'.encode('gbk')}
    try:
        respone = requests.get(url='http://yl.mobsms.net/send/gsend.aspx', params=playload)
        i = respone
    except Exception as e:
        print("send_mobile_error:{}\n".format(e))


if __name__ == '__main__':
    try:
        respone = requests.get(url='https://cggc3.hcmcloud.cn:10151/api/ping_all_alive', timeout=2)
        if respone.text != '{"success": "ok", "message": {"mysql": true, "redis": true}}':
            raise Exception
        send_mobile_warn()
    except Exception as e:
        send_mail_warn()
        print("error:{}\n".format(e))
