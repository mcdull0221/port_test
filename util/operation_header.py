__author__ = 'songxiaolin'
import requests
import json

# url = "https://m.imooc.com/passport/user/login"
# data = {
#     "username": "songxl@nurotron.com",
#     "password": "qqmima123",
#     "verify": "",
#     "referer": "http://m.imooc.com"
# }
# res = requests.post(url, data).json()
# print(res)
# response_url = res['data']['url'][0]
# request_url = response_url + "&callback=jQuery21008240514814031887_1508666806688&_=1508666806689"
# cookie = requests.get(response_url).cookies     # 获取cookies
# print(cookie)
url = "http://139.224.133.194/NRK/AAA/user/login/"
data = {
    "phone_number": "+8613777864459",
    "password": "s1234567"
}
data = json.dumps(data)
print(type(data))
header = {
    "Content-Type": "application/json"
}
res = requests.post(url=url, data=data, headers=header)
print(res)
cookies = requests.utils.dict_from_cookiejar(res.cookies)   # 获取返回的cookies值
print(cookies['sessionid'])


class OperationHerader:
    pass
