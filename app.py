from flask import Flask, redirect, url_for, render_template
#this a simple website in flask, flask is a python framework
app = Flask(__name__)
# this website has three pages
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/tribute')
def tribute():
    return render_template("tribute.html")

if __name__ == "__main__":
    app.run(debug=True)
