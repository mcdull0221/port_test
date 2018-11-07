import requests


class RunMethod:
    def post_main(self, url, data, header=None):
        if header is None:
            res = requests.post(url=url, data=data, headers=header).text
        else:
            res = requests.post(url=url, data=data).text
        return res

    def get_main(self, url, data, header=None):
        if header is None:
            res = requests.get(url=url, data=data, headers=header).text
        else:
            res = requests.get(url=url, data=data).text
        return res

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return res
