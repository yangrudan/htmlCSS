import time

from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

UUUU = {
    '1':{'name':'王','count':1},
    '2':{'name':'李','count':1},
    '3':{'name':'赵','count':1},
}

@app.route('/get_all')
def get_all():
    print("ok==")
    return "ok"

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html',user_list = UUUU, val='empty')


@app.route('/get_sth', methods=['GET', 'POST'])
def get_sth():
    if request.method == 'POST':
        if request.form['action'] == 'get_all':
            val = get_all()
            print("Get_all-=====")
    print(f"ok this is {val}")
    # time.sleep(10)
    return render_template('index.html',user_list = UUUU, val = val)


@app.route('/m112',methods=['GET','POST'])
def m112():
   res = 11111
   return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)