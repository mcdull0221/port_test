__author__ = 'songxiaolin'
import requests
import json
from util.operate_json import OperationJson
# url = "http://139.224.133.194/NRK/AAA/user/login/"
# data = {
#     "phone_number": "+8613777864459",
#     "password": "s1234567"
# }
# data = json.dumps(data)
# print(type(data))
# header = {
#     "Content-Type": "application/json"
# }
# res = requests.post(url=url, data=data, headers=header)
# print(res)
# cookies = requests.utils.dict_from_cookiejar(res.cookies)   # 获取返回的cookies值将cookiejar类型转换成字典类型
# print(cookies['sessionid'])


class OperationHerader:
    def __init__(self, response):
        self.response = response

    # def get_response_url(self):
    #     '''
    #     获取登录返回的token的url
    #     '''
    #     url = self.response['data']['url'][0]
    #     return url

    def get_cookie(self):
        '''
        获取cookie
        '''
        cookie = requests.utils.dict_from_cookiejar(self.response.cookies)
        return cookie

    def write_cookie(self):
        op_json = OperationJson()
        op_json.write_json_data(self.get_cookie())

    # # 组合成新的header
    # def new_header(self, key=None):
    #     header = {
    #         "Content-Type": "application/json"
    #     }
    #     if key is None:
    #         cookie = self.get_cookie()['sessionid']
    #         header['Cookie'] = 'sessionid'+'='+cookie
    #         # print(header)
    #     else:
    #         cookie = self.get_cookie()[key]
    #         header['Cookie'] = key+'='+cookie
    #     return header


if __name__ == '__main__':
    url = "http://139.224.133.194/NRK/AAA/user/login/"
    data = {
        "phone_number": "+8613777864459",
        "password": "s1234567"
    }
    data = json.dumps(data)
    header = {
        "Content-Type": "application/json"
    }
    res = requests.post(url=url, data=data, headers=header)
    op_header = OperationHerader(res)
    op_header.write_cookie()
    # url = 'http://139.224.133.194/NRK/AAA/user/userInfo/'
    # cookie = requests.utils.dict_from_cookiejar(op_header.get_cookie())
    # header = cookie
    # res = requests.get(url=url, data=None, headers=header)
    # print(res.json())
