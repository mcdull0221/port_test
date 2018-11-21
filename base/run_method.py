import requests
import json


class RunMethod:
    def __init__(self):
        self.header = {
        "Content-Type": "application/json"
    }

    def post_main(self, url, data, header=None):
        if header is None:
            res = requests.post(url=url, data=data, headers=self.header)
        else:
            res = requests.post(url=url, data=data, headers=header)
        # print(res.status_code)    # 状态码
        # return res.json()
        return res

    def get_main(self, url, data=None, header=None):
        if header is None:
            res = requests.post(url=url, data=data, headers=self.header)
        else:
            res = requests.post(url=url, data=data, headers=header)
        print(header)
        print(data)
        # print(res.status_code)  # 状态码
        # return res.json()
        print(res.json())
        return res

    def run_main(self, method, url, data=None, header=None):
        res = None
        data = json.dumps(data)
        if method == 'post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        # return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
        return res


if __name__ == '__main__':
    run_method = RunMethod()
    url = "http://139.224.133.194/NRK/AAA/user/userInfo/"
    res = run_method.run_main('post', url=url)
    print(type(res.json()))
