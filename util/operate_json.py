import json
import requests


class OperationJson:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = '../dataconfig/login.json'
        else:
            self.file_path = file_path
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data

    # 根据关键字获取数据
    def get_data(self, key):
        try:
            value = self.data[key]
            return value
        except KeyError:
            print("请求数据错误")

    # 写入json
    def write_json_data(self, data):
        with open('../dataconfig/cookie.json', 'w') as fp:
            fp.write(json.dumps(data))

    # 组成新的header
    def new_header(self, key=None):
        header = {
            "Content-Type": "application/json"
        }
        if key is None:
            cookie = self.get_data('sessionid')
            header['Cookie'] = 'sessionid'+'='+cookie
        else:
            cookie = self.get_data(key)
            header['Cookie'] = key+'='+cookie
        return header


if __name__ == '__main__':
    opjson = OperationJson()
    # print(opjson.get_data('song'))
    # print(type(opjson.get_data('song')))
    op_json = OperationJson('../dataconfig/cookie.json')
    print(op_json.new_header())
    print(type(op_json.new_header()))
    header = op_json.new_header()
    url = "http://139.224.133.194/NRK/AAA/user/userInfo/"
    # data = {
    #     "phone_number": "+8613777864459",
    #     "password": "s1234567"
    # }
    # data = json.dumps(data)
    res = requests.get(url=url, data=None, headers=header)
    print(res.json())

    # header    {'Content-Type': 'application/json', 'Cookie': 'sessionid=8j2nw2rcdlwouc4i3nwyqaq6lbnf43g8'}
