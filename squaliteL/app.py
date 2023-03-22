from flask import Flask, render_template, request
import sqlite3
"""
https://zhuanlan.zhihu.com/p/546663861
"""
app=Flask(__name__)


@app.route('/addstudent',methods = ['POST', 'GET'])
def add_student():
    try:
        #获取请求中的nm、add、city、pin的数据
        nm = request.form['nm']
        addr = request.form['add']
        city = request.form['city']
        pin = request.form['pin']
        with sqlite3.connect("database.db") as con:  #建立与database.db数据库的连接
           cur = con.cursor()    #获取游标
           cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )     #添加数据，执行单条的sql语句
           con.commit()     #提交事务
           msg = "数据添加成功"
    except:
        con.rollback()    #撤消当前事务中所做的所有更改
        msg = "操作失败"
    finally:
        return render_template("result.html",msg = msg)  #渲染result.html模板并传递msg值
        con.close()     #关闭数据库连接

@app.route('/create')
def create_student():
    return render_template('student.html')  #渲染student.html模板

@app.route('/show')
def show_student():
    con = sqlite3.connect("database.db")  #建立数据库连接
    con.row_factory = sqlite3.Row      #设置row_factory,对查询到的数据，通过字段名获取列数据
    cur = con.cursor()        #获取游标
    cur.execute("select * from students")   #执行sql语句选择数据表
    rows = cur.fetchall()      #获取多条记录数据
    return render_template("show.html",rows = rows)  #渲染show.html模板并传递rows值


if __name__ == '__main__':
    app.run(port=8080,debug=True)