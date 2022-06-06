#!/usr/bin/python
from posixpath import split
from konlpy.tag import Mecab, Kkma, Hannanum, Okt, _komoran
from konlpy.utils import pprint
import pandas as pd
from flask import Flask,render_template,redirect,url_for

#comments = ['나는 학생이다', '진짜 별로다', '아 에어컨 춥다...ㅠㅠ', '행복행', 'hello']  # 다운에게 받는 댓글 리스트
split_list = []  # 유나에게 넘기는 한 댓글 분석한 리스트
preference = {"like": 0, "neutral": 0, "dislike": 0}
word = -2  # like=1 , neutral=0 dislike=-1
global li
li= 0
global ne
ne= 0
global di
di= 0
text=[]
count={}
preferenceCounts=[]
def korean_split(comment):  # 댓글 하나씩 분석해서 어간 list 만들어서 리턴
    tokenizer = Okt()
    split_list = tokenizer.nouns(comment)
    return split_list


def word_count(comments):  # 댓글리스트 모든 댓글 카운트 & top 5개 뽑기

    for comment in comments:  # 댓글 하나씩 넘, 모든 댓글 다 넘길 때까지 반복
        tmp=korean_split(comment)
        text.append(tmp)

    for x in text:
        for y in x:
            count[y]=count.get(y,0)+1

    keyword = pd.Series(count).head()
    keywords = list(keyword.index)
    return keywords

def preference_check(word):
    if (word == 1):
        global li
        li+=1
    elif (word == 0):
        global ne
        ne+=1
    else:
        global di
        di+=1


def cut_word(comments):
    word_count(comments)  # 키워드 총 분석

    for comment in comments:  # 댓글 하나씩 넘, 모든 댓글 다 넘길 때까지 반복
        print(korean_split(comment))  # 유나에게 넘길 리스트
        # 유나한테 선호도 결과 받아옴
        preference_check(word)
    keyword=word_count(comments)
    preference["like"] = li
    preference["neutral"] = ne
    preference["dislike"] = di
    print(keyword)
    print(preference)
    preferenceCounts = list(preference.values())

    return keyword, preferenceCounts
    # 효정에게 keyword, preference 전달
