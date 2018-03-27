from flask import Flask, render_template, request, redirect

app = Flask("MyApp")

# Extra homework
# --------------
# 1. Add some more code to your Python file so that
# visiting localhost:5000/hi returns "Hi" and when
# visiting localhost:5000/bye returns "Goodbye"

@app.route('/hi')
def hi():
    return "Hi"


@app.route('/bye')
def bye():
    # I am using here a debugger message, so try to access
    # the /bye route in your browser and check what will
    # be the output in your terminal. You should be able
    # to see the "I am in the bye() method" message in your
    # terminal. If you somehow do not see it, make sure
    # you started the app with debug=true:
    # app.run(debug=True)
    app.logger.debug("I am in the bye() method")
    return "Goodbye"


# 2. What change would you have to make to your Python file from today's
# session (not your HTML file) for your browser to say "Hello anonymous person!"
# instead of "Hello"?
#
# We do not need the "/" route definition anymore as we are gonna make
# sure that when a user tries to access localhost:5000/,
# will return "Hello anonymus" from the template. So comment it out
# the default @app.route("/") like I did few lines below. Of course
# if you have one.

# @app.route("/")
# def hello():
#     return "Hello World"

# Now the routes "/" and "/<name>" will be registered to only one
# method. We can register more routes to only one method, which is
# great as it avoids code duplication. In our case we just have to
# register '/' route and "/<name>" to the hello method. Now this
# method will handle both routes in case the user accesses them.
# More about route registration:
# http://flask.pocoo.org/docs/0.12/api/#url-route-registrations

@app.route("/")
@app.route("/<name>")
# The name=None set up as a parameter in this hello method
# is basically saying that if no name is provided by the
# user then set it to None, which in python means nothing
def hello(name=None):
    # Oke, so now the user accessed either '/' or '/<some_name>'

    # Below I check if there is a name provided, hence the 'if' statement.
    # If there is one, please overwrite it with the title case of it(capitalized).
    # Otherwise do nothing, so name will remain None.
    if name:
        # For example name is mirela, and after the overwrite below
        # name will become Mirela
        name = name.title()

    # Perfect, so now I can pass to the template either nothing(the '/' case)
    # or a title case of the name provided.
    return render_template("hello.html", name=name)

# Actual homework
# ---------------
# We are only going to tackle point 2 from the Homework section from the course materials,
# since is the only one that actually requires us to write some code. Please see below
# the requirement.
# 2. You can use HTML forms to get all sorts of information from visitors to your website,
# including text, email, numbers, dates, and more. You're not limited to just using text fields
# either - you can use input types like radio buttons, tick boxes, etc.
#
# You can approach this however you want, there a an infinite possibilities to extend this.
#
# I will create an example that will redirect you to a registration page and you
# will fill a form and after you submit you will see a message on the same page but
# the form will not appear anymore since you already submitted the data. Please
# use this as a guidance as this is just an exercise for you to play around with templates
# and HTML.

@app.route("/user/register")
def register(name=None, dessert=None, other=None):
    return render_template("register.html")


@app.route("/user/register_submit", methods=["POST"])
def register_submit():
    form_data = request.form
    name = form_data['name']
    dessert = form_data['dessert']

    if name and dessert:
        message = "Hello {}! We are gonna have lots of {} by the end of the course!".format(name.title(), dessert.lower())

    return render_template("register.html", message=message)


@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data["email"]
    return "All OK"


app.run(debug=True)

