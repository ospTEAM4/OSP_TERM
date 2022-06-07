#!/usr/bin/python
#-*- coding: utf-8 -*-
import pymongo
from datetime import datetime

## DB에 insert 및 update 하는 코드
## main문의 like, neutral, dislike, url 받아와야함

# DB 연결
client = pymongo.MongoClient("mongodb+srv://team4:040105@cluster0.vmetcm8.mongodb.net/?retryWrites=true&w=majority")
db = client.team4
collection = db.result

def make_record_element(like, neutral, dislike): # 새로운 결과 record 만들기
    now = datetime.now()
    time_record = {"date_year": now.strftime('%Y'),
    "date_mon": now.strftime('%m'),
    "date_day": now.strftime('%d'),
    "time_hour": now.strftime('%H'),
    "time_min": now.strftime('%M'),
    "time_sec": now.strftime('%S')}

    result_record = {"like":like, "neutral":neutral, "dislike":dislike}

    record_element = {"time_record":time_record, "result_record":result_record}
    return record_element

def insert_new_element(url, record_element): # DB에 새 URL 넣기
    record = [record_element]
    element = {"url":url, "record":record}
    collection.insert_one(element)

def update_element(url, element, record_element): # 기존 URL에 새 결과 UPDATE
    element['record'].append(record_element)
    collection.delete_one({"url":url})
    collection.insert_one(element)
    
def find_url(url): # DB에서 url 찾기. 있으면 해당 data, 없으면 0 반환
    search = collection.find({"url":url})
    for element in search:
        return element
    return 0

if __name__=="__main__":
    # like, neutral, dislike, url이 받아와야하는 값
    like = 30
    neutral = 40
    dislike = 30
    url = "test_url2.com"

    record_element = make_record_element(like, neutral, dislike)

    element = find_url(url)
    if element == 0 :
        insert_new_element(url, record_element)
    else :
        update_element(url, element, record_element)
        
