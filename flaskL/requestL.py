from flask import Flask, render_template

app=Flask(__name__)

@app.route('/register')
def register():
    return render_template('register.html')   #渲染register.html文件

@app.route('/get_data')
def get_data():
    return '提交成功'
if __name__ == '__main__':
    print(app.url_map)
    app.run(port=8080,debug=True)