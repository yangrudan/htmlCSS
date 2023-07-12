from flask_socketio import SocketIO
from flask import Flask, render_template, request

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
connected_sids = set()  # 存放已连接的客户端


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect')
def on_connect():
    connected_sids.add(request.sid)
    print(f'{request.sid} 已连接')


@socketio.on('disconnect')
def on_disconnect():
    connected_sids.remove(request.sid)
    print(f'{request.sid} 已断开')


@socketio.on('message')
def handle_message(message):
    """收消息"""
    data = message['data']
    print(f'{request.sid} {data}')


@app.route('/hello', defaults={'sid': None})
@app.route('/hello/<sid>')
def hello(sid):
    """发消息"""
    if sid:
        if sid in connected_sids:
            socketio.emit('my_response', {'data': f'Hello, {sid}!'}, room=sid)
            return f'已发信息给{sid}'
        else:
            return f'{sid}不存在'
    else:
        socketio.emit('my_response', {'data': 'Hello!'})
        return '已群发信息'


if __name__ == '__main__':
    socketio.run(app)
