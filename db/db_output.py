#!/usr/bin/python
#-*- coding: utf-8 -*-
import pymongo
from datetime import datetime

## DB에서 url 찾기
## main 문의 url 받아와야함
## 결과값 element를 넘겨야함

# DB 연결
client = pymongo.MongoClient("mongodb+srv://team4:040105@cluster0.vmetcm8.mongodb.net/?retryWrites=true&w=majority")
db = client.team4
collection = db.result
    
def find_url(url): # DB에서 url 찾기. 있으면 1, 없으면 0 반환
    search = collection.find({"url":url})
    for element in search:
        return element
    return 0

if __name__=="__main__":
    # url 받아와야함
    url = "test_url.com"

    element = find_url(url)

    if element == 0:
        print("해당 url을 찾을 수 없습니다.")
    else:
        print(element)
        
        # element['url'] : url
        # len(element['record']) : 해당 url 결과 개수
        # element['record'][i]['time_record'] : 결과 저장 시간 dictionary - date_year, date_mon, date_day, time_hour, time_min, time_sec
        # element['record'][i]['result_record] : 결과 dictionary - like, neutral, dislike


        