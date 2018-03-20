 # -*- coding: utf-8 -*-

from flask import Flask
import random

app = Flask("MyApp")

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/hello/<username>')
def hello_username(username):
    return "Hello %s" % username

@app.route('/brownies/<username>')
def brownies_for_user(username):
    brownies_allowed = random.randint(1,10)
    return '%s is allowed to %d brownies today!' % (username, brownies_allowed)

app.run(debug=True)