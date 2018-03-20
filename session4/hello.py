from flask import Flask

app = Flask("MyApp")

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/hello/<username>')
def hello_username(username):
    return "Hello %s" % username

app.run(debug=True)