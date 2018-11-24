__author__ = 'songxiaolin'
import json
import datetime


class OperareJsonDatetime(json.JSONEncoder):
    """
    有时间jsondumps时datetime格式的数据报错
    就是重写构造json类，遇到日期特殊处理
    使用时，调用上面定义的函数即可，如下：
    print json.dumps(self_data, cls=OperareJsonDatetime)
    """
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)
