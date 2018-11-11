from util.operate_excel import OperationExcel
from base.run_method import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse


class DependentData:
    def __init__(self, case_id):
        self.case_id = case_id
        self.operat_excel = OperationExcel()
        self.run_method = RunMethod()
        self.get_data = GetData()

    # 通关caseID来获取该caseID的整行数据
    def get_case_line_data(self):
        rows_data = self.operat_excel.get_rows_data(self.case_id)
        return rows_data

    # 执行依赖测试。获取结果
    def run_dependent(self):
        row = self.operat_excel.get_row_number(self.case_id)
        request_data = self.get_data.get_data_for_json(row)
        header = self.get_data.is_header(row)
        url = self.get_data.get_request_url(row)
        method = self.get_data.get_request_method(row)
        res = self.run_method.run_main(method, url, request_data, header)
        return res

    # 根据依赖的key去获取执行依赖测试case的相应,然后返回
    def get_data_for_key(self, row):
        depend_data = self.get_data.get_depend_key(row)
        respense_data = self.run_dependent()
        json_exe = parse(depend_data)
        madle = json_exe.find(respense_data)
        return [math.value for math in madle][0]
        # math.value for math in madle 增强的for循环 类似于
        # for i in madle:
        #     i.value
