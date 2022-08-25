from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    imgTest = './static/img/sample.jpg'
    return render_template('index.html', img=imgTest)
