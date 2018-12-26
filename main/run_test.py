import sys
import os
curpath = os.path.abspath(os.path.dirname(__file__))
rootpath = os.path.split(curpath)[0]
sys.path.append(rootpath)
from base.run_method import RunMethod
from data.get_data import GetData
from util.comment_util import CommentUtil
from data.dependent_data import DependentData
from util.operation_header import OperationHerader
from util.operate_json import OperationJson
from util.send_email import SendEmail


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.comment_util = CommentUtil()
        self.send_mail = SendEmail()

    # 程序执行
    def go_on_run(self):
        count = self.data.get_case_lines()
        pass_count = []
        fail_count = []
        for i in range(1, count):
            is_run = self.data.get_is_run(i)
            print(i)
            if is_run is True:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                data = self.data.get_data_for_json(i)
                header = self.data.is_header(i)
                expect = self.data.get_expect_data(i)
                # 如果用需要查询数据库则用下面这条
                # expect = self.data.get_expect_data_for_mysql(i)
                depend_case = self.data.is_depend(i)
                if depend_case is not None:
                    depend_data = DependentData(depend_case)
                    # 获取依赖的相应数据
                    depend_response_data = depend_data.get_data_for_key(i)
                    # 获取依赖的key
                    depend_key = self.data.get_depend_filed(i)
                    data[depend_key] = depend_response_data
                if header == 'write':
                    res = self.run_method.run_main(method, url, data)
                    op_header = OperationHerader(res)
                    op_header.write_cookie()
                elif header == 'yes':
                    op_json = OperationJson('../dataconfig/cookie.json')
                    new_header = op_json.new_header()
                    res = self.run_method.run_main(method, url=url, data=data, header=new_header)
                else:
                    res = self.run_method.run_main(method, url, data)
                res = self.comment_util.remate_data(res)
                # 字符串比较用is_contain，字典比较用is_equal_dict
                result = self.comment_util.is_contain(expect, res)
                if result is True:
                    self.data.write_value(i, 'pass')
                    pass_count.append(i)
                else:
                    self.data.write_value(i, res)
                    fail_count.append(i)
        # print(pass_count)
        # print(fail_count)
        # self.send_mail.send_main(pass_count, fail_count)


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()

