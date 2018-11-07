import json


class OperationJson:
    def __init__(self):
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open('../dataconfig/login.json') as fp:
            data = json.load(fp)
            return data

    # 根据关键字获取数据
    def get_data(self, key):
        return self.data[key]


if __name__ == '__main__':
    opjson = OperationJson()
    print(opjson.get_data('user'))
