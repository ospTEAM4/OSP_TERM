import requests
from bs4 import BeautifulSoup
import sqlite3

url="https://en.wikipedia.org/wiki/Web_crawler"
html= requests.get(url)
html.raise_for_status()
soup=BeautifulSoup(html.content,"html.parser")

#p 태그 가져오기 
p_all=soup.find_all('p')
h1_all=soup.find_all('h1')
h2_all=soup.find_all('h2')
h3_all=soup.find_all('h3')

#특수 기호 제외하는 함수 
def clean_wordlist(input_list): 
    output_list = []
    for word in input_list:
        symbols = """!@#$%^&*()_-+={[}]|\;:"‘'·<>?/., """
        for i in range(len((symbols))):
            word = word.replace(symbols[i], '')      
        if len(word) > 0:
            output_list.append(word)
    return output_list

#빈도수 세는 함수 
def counter(input_list):
    word_count = {}
    for word in clean_list:
        if word in  word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

temp =[]
word_list=[]
i=0

for p in p_all:
    temp = p.get_text()
    word_list.extend(temp.upper().split())

for h1 in h1_all:
    temp1= p.get_text()
    word_list.extend(temp1.upper().split())

for h2 in h2_all:
    temp2= p.get_text()
    word_list.extend(temp2.upper().split())

for h3 in h3_all:
    temp3= p.get_text()
    word_list.extend(temp3.upper().split())


clean_list = clean_wordlist(word_list)
word_frequency = counter(clean_list)
word_frequency = sorted(word_frequency.items(), key=lambda x:x[1], reverse=True) #정렬

print(word_frequency)

##db 연결 및 cursor 생성
#db생성 및 연결
connect = sqlite3.connect("temp.db")
#cursur 생성
cursor = connect.cursor();

##테이블 생성
#cursor.execute("CREATE TABLE TEST_TABLE(word TEXT, frequency INTEGER, url TEXT)")

keys = list(word_frequency.keys())
values= list(word_frequency.values())

for x in range(0,len(keys)):
    cursor.execute("INSERT INTO VALUES(?, ?, ?)",(keys[x],values[x],url))
    
connect.commit()
