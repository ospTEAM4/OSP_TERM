# !usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # get 을 통한 전달받은 테이터를 확인
    key1 = request.args.get("urls")
    print(key1)

    return render_template("home.html")

@app.route('/home.html')
def home2():
    return render_template("home.html")

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

if __name__=="__main__":
    app.run(debug=True)

