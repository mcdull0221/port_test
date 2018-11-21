"""
返回各个方法的列数
"""


class GlobalVar:
    Id = 0
    url = 2
    run = 3
    request_way = 4
    header = 5
    case_depend = 6
    data_depend = 7
    field_depend = 8
    data = 9
    expect = 10
    result = 11


# 获取caseid
def get_id():
    return GlobalVar.Id


# 获取url
def get_url():
    return GlobalVar.url


# 是否运行
def get_run():
    return GlobalVar.run


# 获取运行方式
def get_request_way():
    return GlobalVar.request_way


# 获取header
def get_header():
    return GlobalVar.header


# 获取case_depend
def get_case_depend():
    return GlobalVar.case_depend


# 获取data_depend
def get_data_depend():
    return GlobalVar.data_depend


# 获取field_depend
def get_field_depend():
    return GlobalVar.field_depend


# 获取请求数据
def get_data():
    return GlobalVar.data


# 获取expect
def get_expect():
    return GlobalVar.expect


# 获取result
def get_result():
    return GlobalVar.result


if __name__ == '__main__':
    print(get_field_depend())
