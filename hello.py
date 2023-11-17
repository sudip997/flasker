from flask import Flask, render_template

# create a flask instance
app = Flask(__name__)

# create a route decorator


@app.route('/')
# def index():
# 	return "<h1>Hello World !</h1>"
def index():
    first_name = "Ravi"
    stuff = "This is <strong>Bold</strong> text"
    favorite_pizza = ['Pepperoni', 'Cheese', 'Mushrooms', 41]
    return render_template("index.html", first_name=first_name, 
                           stuff=stuff, 
                           favorite_pizza=favorite_pizza)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

# Create custom error pages
#
# Invalid Url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
