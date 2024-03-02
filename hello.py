from flask import Flask

app = Flask(__name__)

print(__name__)


def make_bold(function):
    def wrapper():
        text = function()
        return (f"<b>{text}</b>")
    return wrapper

def make_italic(function):
    def wrapper():
        return "<i>" + function() + "</i>"
    return wrapper

def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper



@app.route("/bye")
@make_bold
@make_italic
@make_underline
def bye():
    return "Bye"


@app.route("/")
def hello_world():
    return ("<h1 style='text-align: center'>Hello, World!</h1>"
            "<p style='text-align: left'>This is a paragraph.</p>"
            "<img src='https://media.giphy.com/media/JOe1P4jUAhTKhPI787/giphy.gif'/>")



@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello, {name}, you are {number} years old"






if __name__ == "__main__":
    app.run(debug=True)


# Decorater code

import time

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970


# decorator wrapper below 👇

def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        run_time = end_time - start_time
        print(f"{function.__name__} run speed: {run_time}s")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


fast_function()
slow_function()


""" 
# Exercise with advanced decorators

def logging_decorator(function):
  def wrapper(*args):
    print(f"You called {function.__name__}({args[0]}, {args[1]}, {args[2]})")
    result=function(args[0],args[1],args[2])
    print(f"It returned: {result}")
  return wrapper

# TODO: Use the decorator 👇

@logging_decorator
def a_function(a, b, c):
  return a * b * c

a_function(inputs[0], inputs[1], inputs[2])
"""