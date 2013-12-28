__author__ = 'jonathan'
#coding=utf-8
#导入需要数据库
import sqlite3
#1.建立与数据库连接
connection = sqlite3.connect('test.db')
#2创建数据游标
cursor = connection.cursor()
#3执行一些sql操作
cursor.execute("select date('NOW')")
print(cursor.fetchone())
#4提交所做的修改，使修改永久保留
connection.commit()
#5完成时关闭链接
connection.close()