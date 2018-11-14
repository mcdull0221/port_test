from base.run_method import RunMethod
from data.get_data import GetData
from util.comment_util import CommentUtil
import sys
from data.dependent_data import DependentData
from util.send_email import SendEmail
sys.path.append("E:/pythonProject/porttest")


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
            if is_run is True:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                data = self.data.get_data_for_json(i)
                header = self.data.is_header(i)
                expect = self.data.get_expect_data(i)
                depend_case = self.data.is_depend(i)
                if depend_case != '':
                    depend_data = DependentData(depend_case)
                    # 获取依赖的相应数据
                    depend_response_data = depend_data.get_data_for_key(i)
                    # 获取依赖的key
                    depend_key = self.data.get_depend_filed(i)
                    data[depend_key] = depend_response_data
                res = self.run_method.run_main(method, url, data, header)

                result = self.comment_util.is_contain(expect, res)
                if result is True:
                    self.data.write_value(i, 'pass')
                    pass_count.append(i)
                else:
                    self.data.write_value(i, res)
                    fail_count.append(i)
        # print(pass_count)
        # print(fail_count)
        self.send_mail.send_main(pass_count, fail_count)


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()

