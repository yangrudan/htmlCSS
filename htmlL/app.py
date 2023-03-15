# -*- coding: utf-8 -*-
"""
@Time:        2022/12/2 17:11
@Author:      CookieYang
@FileName:    myTest.py
@SoftWare:    PyCharm
@brief:       尝试使用Flask
"""

from flask import *

app=Flask(__name__)

@app.route('/')      #设置根目录路由
def hello():
    return render_template('HeadFirstLounge.html')


@app.route('/index',methods=['GET','POST'])    #获取表单（模板）并渲染
def index():
    return render_template('HeadFirstLounge.html')


if __name__ == '__main__':
    app.run(debug=True)

