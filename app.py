# !usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import google_keyword
import cut_word
app = Flask(__name__)

@app.route('/')
def home():
    # get 을 통한 전달받은 테이터를 확인

    key1 = request.args.get("urls")
    print(key1)
    if key1 is None:
        print('!!!')
        return render_template('home.html')
    else:
        comment=google_keyword.result(key1)
        keyword,preference=cut_word.cut_word(comment)
        print(111)

    return render_template("home.html",keyword=keyword,preference=preference)

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

