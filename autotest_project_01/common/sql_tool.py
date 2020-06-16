import pymysql
from autotest_project_01.common.config_read import my_conf


# 把逻辑代码放到方法中,然后思考方法的参数!
#     思考,哪些作为参数!


class SQLTools():

    def __init__(self): # 建立连接时候,就会开启一个事务!
        self.connection = pymysql.connect(
            host=my_conf.get('mysql','host'),
            user=my_conf.get('mysql','user'),
            password=my_conf.get('mysql','password'),
            database=my_conf.get('mysql','database'),
            port=my_conf.getint('mysql','port')
        )
        self.cursor = self.connection.cursor()

    def select_one(self, sql):
        self.connection.commit()
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def select_all(self,sql):
        self.connection.commit()
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def select_count(self,sql):
        self.connection.commit()
        result = self.cursor.execute(sql)
        return result

    def delete(self,sql):
        self.connection.commit()
        self.cursor.execute(sql)
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()


if __name__ == '__main__':
    # data = SQLTools().select_all('select * from cola_member')
    # data = SQLTools().select_all('select * from cola_member')
    data = SQLTools().select_one('select * from cola_member where phoneNumber = 13333333333')
    print(data)

    # print(data)