# -*- coding: utf-8 -*-
import pymysql

# 数据库配置
dbinfo = {
    "host": "49.235.92.12",
    "user": "root",
    "password": "123456",
    "port": 3309
}


class DbConnect():
    def __init__(self, db_cof, database=""):
        self.db_cof = db_cof
        self.db = pymysql.connect(database=database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **db_cof)
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

    def select(self, sql):
        """
        # SQL 查询语句 list of dict
        # sql = "SELECT * FROM EMPLOYEE \
        #        WHERE INCOME > %s" % (1000)
        """
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def execute(self, sql):
        # SQL 删除、提交、修改语句
        # sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交修改
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

    def close(self):
        # 关闭连接
        self.db.close()


if __name__ == '__main__':
    db = DbConnect(dbinfo, "online")
    # 删除
    sql2 = 'DELETE FROM users_userprofile WHERE username = "1234573@qq.com";'
    db.execute(sql2)
    sql1 = 'SELECT * from users_userprofile where username="1234573@qq.com";'
    result = db.select(sql1)
    print(result)
