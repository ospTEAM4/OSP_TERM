# !usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import google_keyword
import cut_word
import database
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
        keyword,preference,preferenceRates=cut_word.cut_word(comment)
        database.push_data(key1, preferenceRates)
        element=database.find_data(key1)
        dates=[]
        likes=[]
        dislikes=[]
        neu=[]
        for i in range(0,len(element['record'])):
            x=list(element['record'][i]['time_record'].values())
            tmp=' '.join(s for s in x)
            dates.append(tmp)
            likes.append(element['record'][i]['result_record']['like'])
            dislikes.append(element['record'][i]['result_record']['dislike'])
            neu.append(element['record'][i]['result_record']['neutral'])
        print(111)

    return render_template("home.html",keyword=keyword,preference=preference,element=element,dates=dates,likes=likes,dislikes=dislikes,neu=neu)



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

