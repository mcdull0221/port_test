__author__ = 'songxiaolin'
import smtplib
# 发送字符串类型的邮件
from email.mime.text import MIMEText
# 处理多种形态主题的邮件
from email.mime.multipart import MIMEMultipart
# 处理图片需要MIMEImage
from email.mime.image import MIMEImage
from email.header import Header
import time
import os,sys


class SendEmail:
    # global send_user
    # global email_host
    # global password
    email_host = "smtp.163.com"
    send_user = "13777864459@163.com"
    password = "FFMRJ5XXG5MV"       # 授权码

    def send_mail(self, user_list, sub, content):
        user = "PortTest" + "<" + SendEmail.send_user + ">"
        # message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message = MIMEMultipart()
        message['Subject'] = sub        # 标题
        message['From'] = user
        message['To'] = ";".join(user_list)
        # 邮件正文内容
        message.attach(MIMEText(content, _subtype='plain', _charset='utf-8'))
        # 构建附件测试报告，传送当前文件
        att1 = MIMEText(open('../dataconfig/case1.xls', 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # att1["Content-Disposition"] = 'attachment; filename="case.xls"'
        att1["Content-Disposition"] = 'attachment; filename="case.xls"'
        message.attach(att1)
        try:
            server = smtplib.SMTP()
            server.connect(SendEmail.email_host)
            server.login(SendEmail.send_user, SendEmail.password)
            server.sendmail(user, user_list, message.as_string())
            server.close()
        except smtplib.SMTPException:
            print("无法发送邮件")

    def send_main(self, pass_list, fail_list):
        """
        :param pass_list: 通过的用例列
        :param fail_list: 失败的用例列
        :return:
        """
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        pass_result = "%.2f%%" % (pass_num/count_num*100)
        fail_result = "%.2f%%" % (fail_num/count_num*100)

        user_list = ['603561287@qq.com']
        sub = time.strftime('%Y-%m-%d %H:%M', time.localtime())+"接口自动化测试报告"
        content = "此次一共运行的接口个数为%s个，通过个数为%s个，失败个数为%s，通过率为%s，" \
                  "失败率为%s" % (count_num, pass_num, fail_num, pass_result, fail_result)
        self.send_mail(user_list, sub, content)


if __name__ == '__main__':
    # send = SendEmail()
    # send.send_main([1,2,3,4], [2,1,5,4,6])
    ti = time.strftime('%Y-%m-%d %H:%M', time.localtime())+"接口自动化测试报告"
    print(ti)



