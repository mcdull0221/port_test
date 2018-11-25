import requests
import json


class RunMethod:
    def __init__(self):
        self.header = {
        "Content-Type": "application/json"
    }

    def post_main(self, url, data, header=None):
        if header is None:
            res = requests.post(url=url, data=data, headers=self.header, verify=False)
        else:
            res = requests.post(url=url, data=data, headers=header, verify=False)
        # print(res.status_code)    # 状态码
        # return res.json()
        return res

    def get_main(self, url, data=None, header=None):
        if header is None:
            res = requests.get(url=url, data=data, headers=self.header, verify=False)
        else:
            res = requests.get(url=url, data=data, headers=header, verify=False)
        # print(res.status_code)  # 状态码
        # return res.json()
        return res

    def put_main(self, url, data, header=None):
        if header is None:
            res = requests.put(url=url, data=data, headers=self.header, verify=False)
        else:
            res = requests.put(url=url, data=data, headers=header, verify=False)
        return res

    def delete_main(self, url, data, header=None):
        if header is None:
            res = requests.delete(url=url, data=data, headers=self.header, verify=False)
        else:
            res = requests.delete(url=url, data=data, headers=header, verify=False)
        return res

    def run_main(self, method, url, data=None, header=None):
        if data is not None:
            data = json.dumps(data)
        if method == 'post':
            res = self.post_main(url, data, header)
        elif method == 'get':
            res = self.get_main(url, data, header)
        elif method == 'put':
            res = self.put_main(url, data, header)
        else:
            res = self.delete_main(url, data, header)
        # return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
        return res


if __name__ == '__main__':
    run_method = RunMethod()
    urls = "http://139.224.133.194/NRK/AAA/user/userInfo/"
    response = run_method.run_main('post', url=urls)
    print(type(response.json()))
