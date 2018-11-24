from filecmp import cmp

__author__ = 'songxiaolin'
import json


class CommentUtil:
    def __init__(self):
        pass

    def remate_data(self, data):
        """
        :param data:  请求返回的response
        :return:字符串后的类型
        """
        res = data.json()
        new_data = json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
        return new_data

    def is_contain(self, str_one, str_two):
        """
        判断一个字符串是否在另一个字符串中
        str_one:查找的字符串
        str_two:被查找的字符串
        :return:
        """
        flag = None
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

    def is_equal_dict(self, dict_one, dict_two):
        """
        判断两个字典是否相等
        如果是字符串则先转换为字典
        """
        if isinstance(dict_one, str):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two, str):
            dict_two = json.loads(dict_two)
        return cmp(dict_one, dict_two)

