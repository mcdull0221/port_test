__author__ = 'songxiaolin'
import smtplib
from email.mime.text import MIMEText


class SendEmail:
    global send_user
    global email_host
    global password
    email_host = "smtp.163.com"
    send_user = "13777864459@163.com"
    password = "FFMRJ5XXG5MV"       # 授权码

    def send_mail(self, user_list, sub, content):
        user = "Mushishi" + "<" + send_user + ">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub        # 标题
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, user_list, message.as_string())
        server.close()


if __name__ == '__main__':
    send = SendEmail()
    user_list = ['603561287@qq.com']
    sub = "测试邮件"
    content = "第一封测试邮件"
    send.send_mail(user_list, sub, content)

