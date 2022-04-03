
from flask import Flask, redirect, url_for, render_template, request

#this a simple website in flask, flask is a python framework

app = Flask(__name__)

# this website has three pages

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
