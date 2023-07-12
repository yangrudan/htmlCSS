from flask import Flask, render_template

app=Flask(__name__)

@app.route('/macro')
def use_macro():
    return render_template('macro1.html')

if __name__ == '__main__':
    app.run(port=8080,debug=True)