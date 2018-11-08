__author__ = 'songxiaolin'
from data import data_config
from util.operate_excel import OperationExcel
from util.operate_json import OperationJson


class GetData:
    def __init__(self):
        self.opera_excel = OperationExcel()

    # 获取excel行数，=case数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取是否会执行
    def get_is_run(self, row):
        flag = None
        col = data_config.get_run()
        run_model = self.opera_excel.get_cell(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header
    def is_header(self, row):
        col = data_config.get_header()
        header = self.opera_excel.get_cell(row, col)
        if header == 'yes':
            return 'header'
        else:
            return None

    # 获取请求方式
    def get_request_method(self, row):
        col = data_config.get_request_way()
        request_method = self.opera_excel.get_cell(row, col)
        return request_method

    # 获取url
    def get_request_url(self, row):
        col = data_config.get_url()
        url = self.opera_excel.get_cell(row, col)
        return url

    # 获取请求数据
    def get_request_data(self, row):
        col = data_config.get_data()
        data = self.opera_excel.get_cell(row, col)
        if data is None:
            return None
        else:
            return data

    # 通过获取关键字拿到data数据
    def get_data_for_json(self, row):
        opera_json = OperationJson()
        request_data = opera_json.get_data(self.get_request_data(row))
        return request_data

    # 获取预期结果
    def get_expect_data(self, row):
        col = data_config.get_expect()
        expect_data = self.opera_excel.get_cell(row, col)
        if expect_data is None:
            return None
        else:
            return expect_data


if __name__ == '__main__':
    get_data = GetData()
    data = get_data.get_data_for_json(1)
    print(data)

