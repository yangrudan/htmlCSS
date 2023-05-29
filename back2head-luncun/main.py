import time
import threading

from flask_cors import CORS
from flask import Flask, redirect, render_template

app = Flask(__name__)
# cors = CORS(app)

job = {}  # 任务状态


def do_job(id):
    global job
    job[id] = 'doing'
    time.sleep(5)
    job[id] = 'done'


@app.route('/job/<id>', methods=['POST'])
def create(id):
    """创建任务"""
    threading.Thread(target=do_job, args=(id,)).start()
    response = redirect(f'/job/{id}')  # 重定向到查询该任务状态
    return response


@app.route('/job/<id>', methods=['GET'])
def status(id):
    """查询任务状态"""
    return job.get(id, 'not exist')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
