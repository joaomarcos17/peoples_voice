from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello welcome to people's voice</h1>"

@app.route('/about')
def about():
    return "<h1>About people's voice</h1>"


if __name__ == "__main__":
    app.run(debug=True)
