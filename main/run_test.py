import sys
sys.path.append("E:/pythonProject/porttest")
from base.run_method import RunMethod
from data.get_data import GetData


class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()

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
            if is_run is True:
                res = self.run_method.run_main(method, url, data, header)
                print(res)


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()

