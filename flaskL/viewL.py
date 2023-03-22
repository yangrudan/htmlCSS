from flask.views import View
from flask import Flask, request

class index(View):  # inherit View
    methods = ["GET", "POST"]
    def get(self):
        return "get"
    def post(self):
        return "post"
    def dispatch_request(self):
        request_method = {"get": self.get, "post": self.post}
        view = request_method.get(request.method.lower())
        return view()

app = Flask(__name__)
app.add_url_rule("/index",view_func=index.as_view("index"))

if __name__ == '__main__':
    app.run(debug=True)