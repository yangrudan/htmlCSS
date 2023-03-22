from flask import Flask, render_template

app=Flask(__name__)

#展示父模板页面
@app.route('/base')
def load_base():
    return render_template('base.html')

# 展示子模板页面
@app.route('/')
def index():
    return render_template('son.html')


if __name__ == '__main__':
    app.run(port=8080,debug=True)