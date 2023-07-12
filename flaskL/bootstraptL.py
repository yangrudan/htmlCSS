from flask import Flask, render_template
from flask_bootstrap import Bootstrap4


app = Flask(__name__)
bootstrap = Bootstrap4(app)


@app.route('/')
def index():
    return render_template('mybase.html')

if __name__ == '__main__':
    app.run()