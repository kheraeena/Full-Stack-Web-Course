from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/about")
def about():
    return "This is an about me page"


@app.route("/contactus")
def contactus():
    return "This is our contact info"


if __name__=='__main__':
    app.run(debug=True)
