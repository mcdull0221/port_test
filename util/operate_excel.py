import xlrd
import xlwt
from xlutils.copy import copy
import sys, os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class OperationExcel:
    def __init__(self, file_path=None, sheet_id=None):
        if file_path:
            self.file_path = file_path
            self.sheet_id = sheet_id
        else:
            self.file_path = PATH('../dataconfig/case1.xls')
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取Excel数据
    def get_data(self):
        data = xlrd.open_workbook(self.file_path)
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_lines(self):
        """获取行数"""
        tables = self.get_data()
        return tables.nrows

    # 获取某一个单元格的内容
    def get_cell(self, row, col):
        return self.data.cell_value(row, col)

    # 写入数据到Excel
    def write_value(self, row, col, value):
        """
        :param row: 行
        :param col:列
        :param value:写入的值
        :return:
        """
        excel = xlrd.open_workbook(self.file_path)
        excel_copy = copy(excel)
        sheet_data = excel_copy.get_sheet(0)
        sheet_data.write(row, col, value)
        excel_copy.save(self.file_path)


if __name__ == '__main__':
    opers = OperationExcel()
    print(opers.get_lines())
    print(opers.get_cell(1, 10))
    opers.write_value(2, 12, '123123')
