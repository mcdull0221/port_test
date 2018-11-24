__author__ = 'songxiaolin'
import pymysql
import pymysql.cursors
import json


# db = pymysql.connect('localhost', 'root', '123456', 'redmine')
# cursor = db.cursor()
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print(data)
class ConnectDb:
    """
    # 打开数据库连接
    db = pymysql.connect("localhost","testuser","test123","TESTDB" )
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    # 关闭数据库连接
    db.close()
    """
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='redmine',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor  # 如果不加这个，打印出来的result为元组，  加上这个 打印的result 结果为列表里面包含字典。
        )
        self.cur = self.conn.cursor()

        # 查询一条数据

    def search_one(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        # result = json.dumps(result)
        return result


if __name__ == '__main__':
    op_mysql = ConnectDb()
    res = op_mysql.search_one("select * from users where id=5")
    print(res)
    print(type(res))



