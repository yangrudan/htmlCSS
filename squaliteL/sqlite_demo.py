import sqlite3
conn = sqlite3.connect('database.db')  #建立database.db数据库连接
conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)') #执行单条sql语句
conn.close()       #关闭连接