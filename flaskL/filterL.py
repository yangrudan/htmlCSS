"""
{{  变量名 | 过滤器  }}
{{  变量名 | 过滤器(参数)}}
"""


from flask import Flask, render_template

app=Flask(__name__)

@app.route('/index')
def index():
    msg='<h1>欢迎学习Flask框架</h1>'    #带有h1标签的字符串
    return render_template('filter_show.html',msg=msg) #渲染show2.html并传入msg参数

if __name__ == '__main__':
    app.run(port=8080,debug=True)