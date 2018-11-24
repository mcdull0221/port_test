__author__ = 'songxiaolin'
from data import data_config
from util.operate_excel import OperationExcel
from util.operate_json import OperationJson
from util.connect_db import ConnectDb


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
        if header != '':
            return header
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
        if data == '':
            return ''
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
        if expect_data == '':
            return None
        return expect_data

    # 通过sql获取预期结果
    def get_expect_data_for_mysql(self, row):
        sql = self.get_expect_data(row)
        op_mysql = ConnectDb()
        res = op_mysql.search_one(sql)
        return res
        # 如果没有显示中文则需要转译
        # return res.decode('unicode-escape')

    # 获取依赖数据的key
    def get_depend_key(self, row):
        col = data_config.get_data_depend()
        depent_key = self.opera_excel.get_cell(row, col)
        if depent_key == '':
            return None
        else:
            return depent_key

    # 将测试结果写入到Excel中
    def write_value(self, row, value):
        col = data_config.get_result()
        self.opera_excel.write_value(row, col, value)

    # 判断是否有case依赖
    def is_depend(self, row):
        col = data_config.get_case_depend()
        # print(col)
        depend_case_id = self.opera_excel.get_cell(row, col)
        # print(type(depend_case_id))
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    # 获取数据依赖字段
    def get_depend_filed(self, row):
        col = data_config.get_field_depend()
        data = self.opera_excel.get_cell(row, col)
        if data == "":
            return None
        else:
            return data


if __name__ == '__main__':
    get_data = GetData()
#     data = get_data.get_data_for_json(1)
#     # print(data)
#     print(get_data.is_depend(1))
    data = get_data.get_expect_data_for_mysql(1)
    print(data)

