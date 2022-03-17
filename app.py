
from flask import Flask, redirect, url_for, render_template, request
#this a simple website in flask, flask is a python framework
app = Flask(__name__)
# this website has three pages
@app.route('/')
def index():
    return render_template("index.html", content="Testing")
@app.route('/tribute')
def tribute():
    return render_template("tribute.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/news')
def news():
    return render_template("news.html")
@app.route('/webapp')
def webapp():
    return render_template("webapp.html")

# form

@app.route('/log')
def log():
    return render_template("get.html") 

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form["nm"]
        return redirect(url_for("user",usr=user))
    else:
        return render_template("login.html")

@app.route('/<usr>')
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
