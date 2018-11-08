import sys
sys.path.append("E:/pythonProject/porttest")
from base.run_method import RunMethod
from data.get_data import GetData
from util.comment_util import CommentUtil


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.comment_util = CommentUtil()

    # 程序执行
    def go_on_run(self):
        res = None
        count = self.data.get_case_lines()
        for i in range(1, count):
            url = self.data.get_request_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_data_for_json(i)
            header = self.data.is_header(i)
            expect = self.data.get_expect_data(i)
            if is_run is True:
                res = self.run_method.run_main(method, url, data, header)
                print(res)
                result = self.comment_util.is_contain(expect, res)
                if result is True:
                    print('测试通过')
                else:
                    print('测试失败')


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()

