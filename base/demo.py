import requests
import json


class RunMain:

    def send_get(self, url, data):
        res = requests.get(url=url, data=data).text
        return res

    def send_post(self, url, data):
        res = requests.post(url=url, data=data).text
        return res

    def run_main(self, url, method, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res


if __name__ == '__main__':
    run = RunMain()
    url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html?cart=11'
    data = {
        'cart': '11'
    }
    run = run.run_main(url, 'GET', data)
    print(run)

# print run.run_main(url,'GET',data)