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

@app.route('/')
def index():
    return render_template('HeadFirstLounge.html')


@app.route('/elixir')
def elixir():
    return render_template('elixir.html')


@app.route('/direction')
def direction():
    return render_template('direction.html')




if __name__ == '__main__':
    app.run(debug=True)

